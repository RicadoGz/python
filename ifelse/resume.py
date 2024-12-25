from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load the original PDF to extract content
uploaded_file_path = "./Dec19 c and python.pdf"
reader = PdfReader(uploaded_file_path)
original_content = "".join([page.extract_text() for page in reader.pages])

# Translation of the extracted text to Chinese
translated_content = """
约翰·多伊的简历

Ricardo Gao
滑铁卢，加拿大 | gaozhe0011@gmail.com | +1 382 885 2156 | https://www.ricardogao.me/

www.linkedin.com/in/ricardo-gao | https://github.com/RicadoGz

技能
网页开发：C#，HTML，CSS，JavaScript，Django，React，网页抓取，HTTP，用户界面设计，网络服务，Selenium
编程与数据管理：Python，面向对象编程（OOP），SQL，Git，Power Automate，MySQL，R，C#，C++，Dart，Go，JSON，Pandas，数据结构，数据科学，数据分析，Requests，Matplotlib，Visual Studio，Excel
云、DevOps和网络：Google Cloud，GitHub，REST API，Linux，CI/CD，测试，安全性，防火墙，故障排除

教育背景
Conestoga College — 软件工程技术 (GPA: 3.93/4.0)

专业经验
C语言编程助学导师 (2025年1月至2025年4月)
• 专注于帮助一年级学生掌握编程基础，尤其是C语言。我组织学习活动并提供指导，以帮助学生理解关键概念、发展解决问题的能力，并提升其编程技能。

Google开发者学生俱乐部执行负责人
• 引入来自Google的最新技能和课程，策划并举办各种工作坊和活动，帮助学生将理论与实践结合。
• 提供指导，帮助学生建立联系、学习并共同成长；共同管理一个超过500人的社团，这也是Conestoga College最大的俱乐部。

项目经验
学生管理系统开发
• https://github.com/RicadoGz/student-manage-version8
• 使用C/C++实现了学生管理程序，包括添加、搜索、修改记录以及保存/加载文件功能。模块化编程、文件处理和错误管理。
• 优化了数据结构和排序算法，数据效率提升了30%，文件操作速度提高了20%。

GPA计算优化
• https://github.com/RicadoGz/student-manage-version8
• 开发了一个GPA计算器，采用输入验证、异步数据处理和加权GPA计算。处理时间减少了40%，进一步优化后效率又提高了15%。

Flappy Bird的神经遗传AI优化
• https://github.com/RicadoGz/AI
• 使用Python、Pygame和NEAT算法开发了Flappy Bird AI。通过400多行代码实现了基于遗传算法的神经网络优化。
• 通过广泛的测试和优化，加快了NEAT算法的收敛速度（提升50%），并增强了AI的适应能力（提升40%）。

全栈RSI股票分析开发
• https://github.com/RicadoGz/own-web
• 使用网页抓取、JavaScript和Flask HTTP创建了全面的股票分析工具的网页功能。
• 实现了异步协程和Matplotlib，数据处理时间减少了70%，进一步改进后又节省了30%的时间。

认证经验
CS50’s Python编程入门课程 – 滑铁卢，ON (2024年6月至2024年7月)
• 涵盖了函数伪代码、操作符、作用域、随机数、import、from、统计学、命令行参数、系统、切片、包、PyPI、pip、API、请求、JSON、pytest、排序、CSV、正则表达式、类、对象、属性、实例变量生成器等内容。
"""

# Output translated PDF
output_pdf_path = "./Translated_Resume.pdf"
packet = canvas.Canvas(output_pdf_path, pagesize=letter)

# Add the translated content to the new PDF
for idx, line in enumerate(translated_content.split("\n")):
    packet.drawString(50, 800 - (idx * 12), line)

packet.save()
output_pdf_path
