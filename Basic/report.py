from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# register the font
pdfmetrics.registerFont(TTFont('SimSun', 'fonts/simsun.ttf'))


class Graphs:
    def __init__(self):
        pass

    @staticmethod
    def draw_title(title, font_size):
        style = getSampleStyleSheet()
        ct = style['Normal']
        ct.fontName = 'SimSun'
        ct.fontSize = font_size
        # 行距
        ct.leading = 40
        ct.textColor = colors.green
        ct.alignment = 1
        title = Paragraph(title, ct)
        return title

    @staticmethod
    def draw_text(text):
        style = getSampleStyleSheet()
        ct = style['Normal']
        ct.fontName = 'SimSun'
        ct.fontSize = 9
        ct.wordWrap = 'CJK'
        ct.alignment = 0
        ct.leading = 30
        text = Paragraph(text, ct)
        return text

    @staticmethod
    def draw_table(*args):
        col_width = 90
        style = [('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 字体
                 ('BACKGROUND', (0, 0), (-1, 0), '#d5dae6'),  # 设置第一行背景颜色
                 ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 对齐
                 ('VALIGN', (-1, 0), (-2, 0), 'MIDDLE'),  # 对齐
                 ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5
                 ]
        table = Table(args, colWidths=col_width, style=style)
        return table


def write2pdf(fields, info, fields_contents):
    batch, _, pro_name, _, _ = info
    filename = pro_name + '-' + batch
    content = list()

    # add title
    content.append(Graphs.draw_title('安徽滁州德威新材料有限公司', 12))
    content.append(Graphs.draw_title('不合格品处理单', 14))
    data = [fields, info]
    content.append(Graphs.draw_table(*data))

    # add paragraph
    for k, v in fields_contents.items():
        content.append(Graphs.draw_text('{}: {}'.format(k, v)))

    doc = SimpleDocTemplate(r'output\{}.pdf'.format(filename), pagesize=A4)
    doc.build(content)

