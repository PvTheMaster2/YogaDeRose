import img2pdf
import os
from PIL import Image

def convert_png_to_pdf(input_path: str, output_path: str = None) -> str:
    """
    Convert a PNG image to PDF format using img2pdf.
    
    Args:
        input_path: Path to the input PNG file
        output_path: Path for the output PDF file (optional)
    
    Returns:
        str: Path to the generated PDF file
    """
    try:
        # Validate input file
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        if not input_path.lower().endswith('.png'):
            raise ValueError("Input file must be a PNG image")
        
        # Check image size
        with Image.open(input_path) as img:
            width, height = img.size
            print(f"Processing image with dimensions: {width}x{height} pixels")
        
        # Generate output path if not provided
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + '.pdf'
        
        # Convert PNG to PDF with layout optimization for large images
        a4_width_mm = 210
        a4_height_mm = 297
        layout_fun = img2pdf.get_layout_fun((a4_width_mm, a4_height_mm))
        
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(input_path, layout_fun=layout_fun))
        
        return output_path
        
    except Exception as e:
        print(f"Error converting image to PDF: {str(e)}")
        raise

def main():
    """Example usage of the converter."""
    try:
        # Use your actual PNG file path
        input_file = "C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\OBSIDIAN\\OBSIDIAN TCC R00\\OBSIDIAN TCC R00\\utils\\test.png"
        output_file = convert_png_to_pdf(input_file)
        print(f"PDF created successfully: {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()


