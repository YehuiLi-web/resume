from jinja2 import Environment, FileSystemLoader
import markdown

# 加载模板
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("resume.html")

# 读取Markdown内容并转HTML
with open("content/resume.md", "r") as f:
    md_content = f.read()
html_content = markdown.markdown(md_content)

# 渲染模板
output = template.render(
    title="张三的简历",
    name="张三",
    content=html_content
)

# 保存生成的HTML
with open("index.html", "w") as f:
    f.write(output)