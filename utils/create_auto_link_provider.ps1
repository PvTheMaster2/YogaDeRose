# Create Auto-Link Provider for Obsidian
# This script creates a JSON file with all note titles to assist with the "Auto Link Title" plugin
# Author: Claude
# Created: 2025-04-18

# Configuration
$rootDir = "C:\Users\pedro\OneDrive\Área de Trabalho\YOGA TRATADO"
$zettelsDir = Join-Path $rootDir "10 - PERMANENT\Zettels\Yoga"
$outputDir = Join-Path $rootDir ".obsidian\plugins\smart-connections\data"
$outputFile = Join-Path $outputDir "yoga_note_titles.json"

# Create the output directory if it doesn't exist
if (!(Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

# Function to extract title from filename
function Get-NoteTitle {
    param (
        [string]$filename
    )
    
    # Remove numbers and dashes from the beginning
    $title = $filename -replace "^\d+-?", ""
    
    # Remove file extension
    $title = $title -replace "\.md$", ""
    
    # Replace dashes with spaces
    $title = $title -replace "-", " "
    
    # Capitalize first letter of each word
    $title = (Get-Culture).TextInfo.ToTitleCase($title.ToLower())
    
    return $title
}

# Function to extract frontmatter metadata from file
function Get-Frontmatter {
    param (
        [string]$filePath
    )
    
    $content = Get-Content $filePath -Raw
    $metadata = @{}
    
    # Check if file has frontmatter
    if ($content -match "^---\s*\n([\s\S]*?)\n---") {
        $frontMatter = $matches[1]
        
        # Extract key-value pairs
        $frontMatter -split "\n" | ForEach-Object {
            if ($_ -match "^\s*([^:]+):\s*(.*)") {
                $key = $matches[1].Trim()
                $value = $matches[2].Trim()
                $metadata[$key] = $value
            }
        }
    }
    
    return $metadata
}

# Function to build a comprehensive title database
function Build-TitleDatabase {
    $titleDatabase = @()
    
    # Get all markdown files in the Zettels directory
    $files = Get-ChildItem -Path $zettelsDir -Filter "*.md" -Recurse
    
    foreach ($file in $files) {
        $relativePath = "10 - PERMANENT/Zettels/Yoga/" + $file.Name
        $title = Get-NoteTitle -filename $file.Name
        
        # Get frontmatter metadata
        $metadata = Get-Frontmatter -filePath $file.FullName
        
        # Use aliases if available, otherwise use the filename-derived title
        $titles = @($title)
        if ($metadata.ContainsKey("aliases")) {
            $aliases = $metadata["aliases"] -split "," | ForEach-Object { $_.Trim() }
            $titles += $aliases
        }
        
        # Extract first header as an additional title
        $content = Get-Content $file.FullName -Raw
        if ($content -match "(?m)^# (.+)$") {
            $headerTitle = $matches[1].Trim()
            if ($headerTitle -ne $title -and -not $titles.Contains($headerTitle)) {
                $titles += $headerTitle
            }
        }
        
        # Create entry for each title/alias
        foreach ($noteTitle in $titles) {
            $titleDatabase += [PSCustomObject]@{
                path = $relativePath
                title = $noteTitle
                keywords = ($noteTitle -split " ") + ($title -split " ") # Add both title variations as keywords
            }
        }
    }
    
    return $titleDatabase
}

# Function to create auto-complete suggestions file
function Create-AutoCompleteSuggestions {
    $titleDatabase = Build-TitleDatabase
    
    # Convert to the format expected by auto-complete plugins
    $suggestions = @{
        titles = $titleDatabase | ForEach-Object {
            @{
                path = $_.path
                title = $_.title
                keywords = $_.keywords
            }
        }
        lastUpdated = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    }
    
    # Save as JSON
    $suggestionsJson = $suggestions | ConvertTo-Json -Depth 3
    $suggestionsJson | Out-File -FilePath $outputFile -Encoding utf8
}

# Main execution
Write-Host "Starting auto-link provider creation..."

# Create the auto-complete suggestions
Create-AutoCompleteSuggestions

# Print success message
Write-Host "Auto-link provider created successfully."
Write-Host "Output file: $outputFile"
Write-Host "This file can be used by the 'Auto Link Title' plugin to suggest note completions."

# Instructions for use
Write-Host @"

INSTRUCTIONS FOR USE:
1. Make sure the 'Auto Link Title' plugin is installed in Obsidian
2. Configure the plugin to use the generated file as its source
3. When typing '[[' in a note, the plugin will now suggest completions based on all your notes

You can run this script periodically to update the suggestions database when you add new notes.
"@ 