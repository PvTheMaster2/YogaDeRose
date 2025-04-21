# Yoga MOC Update Workflow
# This script automates the maintenance of the Yoga Map of Content (MOC)
# Author: Claude
# Created: 2025-04-18

# Configuration
$rootDir = "C:\Users\pedro\OneDrive\Área de Trabalho\YOGA TRATADO"
$zettelsDir = Join-Path $rootDir "10 - PERMANENT\Zettels\Yoga"
$mocFile = Join-Path $rootDir "30 - MPS OF CONTENT\Yoga MOC.md"
$reportDir = Join-Path $rootDir "00 - INBOX\02 - REPORTS"
$reportFile = Join-Path $reportDir "Yoga_MOC_Update_Report_$(Get-Date -Format 'yyyy-MM-dd').md"

# Create the reports directory if it doesn't exist
if (!(Test-Path $reportDir)) {
    New-Item -ItemType Directory -Path $reportDir | Out-Null
}

# Initialize report content
$reportContent = @"
---
created: $(Get-Date -Format "yyyy-MM-dd'T'HH:mm")
updated: $(Get-Date -Format "yyyy-MM-dd'T'HH:mm")
---
# Yoga MOC Update Report - $(Get-Date -Format "yyyy-MM-dd")

This report was automatically generated to track updates and suggestions for the Yoga MOC.

## Summary

"@

# Function to extract section information from the MOC
function Get-MOCSections {
    $content = Get-Content $mocFile -Raw
    $sections = @{}
    
    # Extract all section links using regex
    $pattern = '\[\[([^\]]+)\]\]'
    $matches = [regex]::Matches($content, $pattern)
    
    foreach ($match in $matches) {
        $link = $match.Groups[1].Value
        # Handle links with display text
        if ($link -match '\|') {
            $parts = $link -split '\|'
            $path = $parts[0].Trim()
            $sections[$path] = $true
        } else {
            $sections[$link] = $true
        }
    }
    
    return $sections
}

# Function to find new notes that aren't in the MOC
function Find-NewNotes {
    $mocSections = Get-MOCSections
    $newNotes = @()
    
    # Get all markdown files in the Zettels directory
    $files = Get-ChildItem -Path $zettelsDir -Filter "*.md" -Recurse
    
    foreach ($file in $files) {
        $relativePath = "10 - PERMANENT\Zettels\Yoga\" + $file.Name
        if (!$mocSections.ContainsKey($relativePath)) {
            $newNotes += $file
        }
    }
    
    return $newNotes
}

# Function to suggest connections between notes based on content similarity
function Find-PotentialConnections {
    $files = Get-ChildItem -Path $zettelsDir -Filter "*.md" -Recurse
    $connections = @()
    
    # Create a simple keyword index for each file
    $fileKeywords = @{}
    
    foreach ($file in $files) {
        $content = Get-Content $file.FullName -Raw
        # Extract keywords (simplified approach)
        $keywords = $content -split '[\s\n\r.,;:!?()[\]{}]' | 
                    Where-Object { $_.Length -gt 4 } | 
                    ForEach-Object { $_.ToLower() }
        $fileKeywords[$file.FullName] = $keywords
    }
    
    # Compare files to find potential connections
    for ($i = 0; $i -lt $files.Count; $i++) {
        $file1 = $files[$i]
        $keywords1 = $fileKeywords[$file1.FullName]
        
        for ($j = $i + 1; $j -lt $files.Count; $j++) {
            $file2 = $files[$j]
            $keywords2 = $fileKeywords[$file2.FullName]
            
            # Find common keywords
            $commonKeywords = $keywords1 | Where-Object { $keywords2 -contains $_ } | Select-Object -Unique
            
            # If there are significant common keywords, suggest a connection
            if ($commonKeywords.Count -ge 5) {
                $connections += [PSCustomObject]@{
                    File1 = $file1.Name
                    File2 = $file2.Name
                    CommonTerms = $commonKeywords.Count
                    Keywords = ($commonKeywords | Select-Object -First 10) -join ", "
                }
            }
        }
    }
    
    return $connections | Sort-Object -Property CommonTerms -Descending
}

# Function to identify topics without adequate connections
function Find-IsolatedTopics {
    $files = Get-ChildItem -Path $zettelsDir -Filter "*.md" -Recurse
    $isolated = @()
    
    foreach ($file in $files) {
        $content = Get-Content $file.FullName -Raw
        # Check for links to other files
        $linkPattern = '\[\[([^\]]+)\]\]'
        $linkMatches = [regex]::Matches($content, $linkPattern)
        
        if ($linkMatches.Count -lt 2) {
            # Extract some context about the file
            $title = $file.Name -replace "\.md$", "" -replace "^\d+-?", ""
            $title = $title -replace "-", " "
            
            # Get first 100 characters of content (excluding frontmatter)
            $contentPreview = $content -replace "(?s)^---.*?---", ""
            $contentPreview = $contentPreview.Substring(0, [Math]::Min(100, $contentPreview.Length)).Trim()
            
            $isolated += [PSCustomObject]@{
                File = $file.Name
                Title = $title
                Preview = $contentPreview
                LinkCount = $linkMatches.Count
            }
        }
    }
    
    return $isolated | Sort-Object -Property LinkCount
}

# Main workflow
Write-Host "Starting Yoga MOC update workflow..."

# 1. Find new notes that need to be added to the MOC
$newNotes = Find-NewNotes
$reportContent += @"

## New Notes to Add to MOC
Found $($newNotes.Count) new notes that are not yet included in the MOC:

"@

if ($newNotes.Count -gt 0) {
    foreach ($note in $newNotes) {
        $title = $note.Name -replace "\.md$", "" -replace "^\d+-?", ""
        $title = $title -replace "-", " "
        $relativePath = "10 - PERMANENT/Zettels/Yoga/" + $note.Name
        
        $reportContent += "- [[${relativePath}|${title}]]`n"
    }
} else {
    $reportContent += "No new notes found.`n"
}

# 2. Suggest connections between notes
$connections = Find-PotentialConnections
$reportContent += @"

## Suggested New Connections
Found $($connections.Count) potential connections between notes:

"@

if ($connections.Count -gt 0) {
    $topConnections = $connections | Select-Object -First 10
    foreach ($connection in $topConnections) {
        $file1 = $connection.File1 -replace "\.md$", "" -replace "^\d+-?", ""
        $file1 = $file1 -replace "-", " "
        
        $file2 = $connection.File2 -replace "\.md$", "" -replace "^\d+-?", ""
        $file2 = $file2 -replace "-", " "
        
        $reportContent += @"
- **$file1** ↔ **$file2**
  - Common terms: $($connection.CommonTerms)
  - Keywords: $($connection.Keywords)

"@
    }
} else {
    $reportContent += "No significant new connections found.`n"
}

# 3. Identify topics without adequate connections
$isolated = Find-IsolatedTopics
$reportContent += @"

## Topics Without Adequate Connections
Found $($isolated.Count) topics with fewer than 2 connections:

"@

if ($isolated.Count -gt 0) {
    foreach ($topic in $isolated) {
        $reportContent += @"
- **$($topic.Title)**
  - File: $($topic.File)
  - Preview: "$($topic.Preview)..."
  - Current link count: $($topic.LinkCount)

"@
    }
} else {
    $reportContent += "No isolated topics found. All notes have at least 2 connections.`n"
}

# Add final recommendations
$reportContent += @"

## Recommended Actions

1. Add the new notes to the appropriate sections in the MOC
2. Review the suggested connections and create links between related notes
3. Enhance the isolated topics with more connections to related concepts

Last update: $(Get-Date -Format "yyyy-MM-dd HH:mm")
"@

# Write the report to a file
$reportContent | Out-File -FilePath $reportFile

Write-Host "MOC update workflow completed."
Write-Host "Report generated at: $reportFile" 