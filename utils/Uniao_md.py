import os
import datetime

def combine_markdown_files(input_dir, output_file=None):
    """
    Combines all markdown files in the specified directory into a single markdown file.
    Each file's content is separated by a header indicating the source file.
    
    Args:
        input_dir (str): Path to the directory containing markdown files
        output_file (str, optional): Path to the output file. If None, a default name is generated.
    
    Returns:
        str: Path to the created output file
    """
    # If no output file specified, create a default one
    if output_file is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(input_dir, f"Combined_Markdown_{timestamp}.md")
    
    # Find all markdown files
    md_files = []
    for filename in os.listdir(input_dir):
        # Skip the script itself and the output file
        if filename.lower().endswith('.md') and not filename.startswith("Combined_Markdown_"):
            md_files.append(os.path.join(input_dir, filename))
    
    if not md_files:
        print(f"No markdown files found in {input_dir}")
        return None
    
    print(f"Found {len(md_files)} markdown files")
    
    # Combine all files
    combined_content = "# Combined Markdown Documents\n\n"
    combined_content += f"*Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
    combined_content += f"*Source directory: {os.path.abspath(input_dir)}*\n\n"
    combined_content += "---\n\n"
    
    for file_path in sorted(md_files):
        filename = os.path.basename(file_path)
        
        # Read file content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add file header and content with clear separation
            combined_content += f"## Document: {filename}\n\n"
            combined_content += f"*Source: {os.path.abspath(file_path)}*\n\n"
            combined_content += "```markdown\n"  # Start code block for better visual separation
            combined_content += content.strip()
            combined_content += "\n```\n\n"  # End code block
            combined_content += "---\n\n"  # Horizontal rule for separation
            
        except Exception as e:
            print(f"Error reading {filename}: {str(e)}")
    
    # Write combined content to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(combined_content)
        print(f"Combined markdown saved to: {output_file}")
        return output_file
    except Exception as e:
        print(f"Error writing to {output_file}: {str(e)}")
        return None

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Combine the files from the script's directory
    output_path = combine_markdown_files(script_dir)
    
    if output_path:
        print(f"Success! All markdown files combined into: {output_path}")

if __name__ == "__main__":
    main() 