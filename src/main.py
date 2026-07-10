import os
import sys
from file_handling import *
from inline_functions import extract_title
from markdown_to_html import *

def generate_page(
    from_path: str,
    template_path: str,
    dest_path: str,
    base_path: str
)-> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    absolute_from_path = os.path.expanduser(from_path)
    absolute_template_path = os.path.expanduser(template_path)
    absolute_dest_path = os.path.expanduser(dest_path)

    markdown_file = open(absolute_from_path, "r")
    template_file = open(absolute_template_path, "r")
    
    markdown = markdown_file.read()
    html_from_md = markdown_to_html_node(markdown).to_html()
    template = template_file.read()
    markdown_file.close()
    template_file.close()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_from_md )
    template = template.replace('href="/', f'href={base_path}').replace('src="/', f'src={base_path}')

    if not os.path.exists(absolute_dest_path):
        dir_name = os.path.dirname(absolute_dest_path)
        os.makedirs(dir_name, exist_ok=True)

    with open(absolute_dest_path, "w") as html:
        html.write(template)

    return None

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, base_path:str) -> None:
    absolute_dir_path_content = os.path.expanduser(dir_path_content)
    for content in os.listdir(absolute_dir_path_content):
        path = os.path.join(dir_path_content, content)
        if os.path.isfile(path) and path.endswith(".md"):
            new_path = os.path.join(dest_dir_path, "index.html")
            generate_page(path, template_path, new_path, base_path)
            continue
        if os.path.isfile(path):
            continue
        new_path = os.path.join(os.path.expanduser(dest_dir_path), content) 
        if not os.path.exists(path):
            os.makedirs(os.path.join(new_path), exist_ok=True)
        
        generate_pages_recursive(path, template_path, new_path, base_path)

    return None
def main() -> int:
    basepath = sys.argv[1] or "/"
    print(basepath)
    copy_src_to_destination(f"../static_site_generator/static/", "../static_site_generator/docs/")
    generate_pages_recursive("../static_site_generator/content/", "../static_site_generator/template.html", "../static_site_generator/docs/", basepath)
    return 0

if __name__ == "__main__":
    main()
