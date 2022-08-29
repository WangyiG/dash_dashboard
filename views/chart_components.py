from dash import html
import feffery_antd_charts as fact
import feffery_antd_components as fac

from models.mock_data import faker


# 面包屑
breadcrumb = fac.AntdBreadcrumb(
                items=[
                    {
                        'title': '仪表盘',
                        'icon': 'antd-dashboard'
                    },
                    {
                        'title': '概览面板',
                        'href': '/#概览面板'
                    }
                ],
                style={
                    'marginBottom': '16px'
                }
            )


# 欢迎词
hello_word = fac.AntdParagraph(
                        '欢迎,用户MangTi',
                        style={
                            'fontSize': '20px'
                        }
                    )


# 分割线
divider = fac.AntdDivider(lineColor='#e5e6eb')



# 指标展示栏
def target_render():
    target = faker.mock_target_data()
    return fac.AntdRow(
                        [
                            fac.AntdCol(
                                fac.AntdSpace(
                                    [
                                        fac.AntdAvatar(
                                            mode='icon',
                                            size=60,
                                            icon=item['icon'],
                                            style={
                                                'backgroundColor': '#f2f3f5',
                                                'fontSize': '36px'
                                            }
                                        ),
                                        fac.AntdSpace(
                                            [
                                                fac.AntdText(
                                                    item['title']
                                                ),
                                                html.Span(
                                                    [
                                                        fac.AntdText(
                                                            item['value'],
                                                            strong=True,
                                                            style={
                                                                'fontSize': '28px',
                                                                'paddingRight': '10px'
                                                            }
                                                        ),
                                                        fac.AntdText(
                                                            item['unit']
                                                        )
                                                    ]
                                                )
                                            ],
                                            direction='vertical',
                                            size=0
                                        )
                                    ]
                                ),
                                span=6,
                                style={
                                    'height': '100%',
                                    'borderRight': '1px solid #e5e6eb' if col < 3 else 'none',
                                    'display': 'flex',
                                    'justifyContent': 'center'
                                }
                            )
                            for col, item in enumerate(target)
                        ],
                        style={
                            'height': '120px'
                        }
                    )


# 图主副标题组件
def chart_title(main='Content Data',sub='(Nearly 1 Year)'):
    return  fac.AntdParagraph(
                        [
                            fac.AntdText(
                                main,
                                style={
                                    'fontSize': '22px',
                                    'paddingRight': '5px'
                                }
                            ),

                            fac.AntdText(
                                sub,
                                style={
                                    'color': '#86909c'
                                }
                            )
                        ]
                    )


# 带标题的折线图
def line_render():
    line = faker.mock_line_data()
    return html.Div(
        [
            chart_title(),
            html.Div(
                fact.AntdArea(
                            data = line,
                            smooth=True,
                            xField='Date',
                            yField='scales',
                            areaStyle={
                                'func': '''
                                        () => {
                                            return {
                                                fill: 'l(270) 0:#ffffff 0.5:#7ec2f3 1:#1890ff',
                                            };
                                        }
                                        '''
                            }
                        ),
                        style={
                            'height': '420px'
                        }
            )
        ]
    )



# 带标题的柱形图
def bar_render():
    bar = faker.mock_bar_data()
    return html.Div(
                            [

                                chart_title('Bar chart','mock_bar_data'),
                                html.Div(
                                        fact.AntdColumn(
                                            data=bar,
                                            # isStack=True,
                                            isGroup=True,
                                            xField='year',
                                            yField='value',
                                            seriesField='type',
                                        ),
                                        style={
                                                'marginTop': '70px'
                                            }   
                                ),

                            ],
                            style={
                                'background': 'white',
                                'borderRadius': '4px',
                                'height': '100%',
                                'padding': '20px'
                            }
                        )

# 带标题的饼图
def pie_render():
    pie = faker.mock_pie_data()
    total = str(sum(x['value'] for x in pie))
    return html.Div(
                            [
                                chart_title('Pie Chart','mock_pie_data'),
                                html.Div(
                                    fact.AntdPie(
                                        # data=pie_demo_data,
                                        data = pie,
                                        angleField='value',
                                        colorField='type',
                                        radius=0.8,
                                        innerRadius=0.5,
                                        color=['#2ccfff','#3c46ad','#2fa3ff'],
                                        label={
                                            'type': 'spider',
                                            'style': {
                                                'fontSize': 18
                                            }
                                        },
                                        statistic={
                                            'title': {
                                                'content': '内容量'
                                            },
                                            'content': {
                                                'content': total
                                            }
                                        },
                                        legend={
                                            'position': 'bottom'
                                        }
                                    ),
                                    style={
                                        'height': 'calc(100% - 45px)'
                                    }
                                )
                            ],
                            style={
                                'background': 'white',
                                'borderRadius': '4px',
                                'height': '100%',
                                'padding': '20px'
                            }
                        )


# 带标题的气泡图
def scatter_render():
    scatter = faker.mock_scatter_data()
    return html.Div(
        [
            chart_title('Scatter chart','mock_scatter_data'),
            fact.AntdScatter(
                                data=scatter,
                                xField='x',
                                yField='y',
                                colorField='genre',
                                color=['r(0.4, 0.3, 0.7) 0:rgba(255,255,255,0.5) 1:#5B8FF9','r(0.4, 0.4, 0.7) 0:rgba(255,255,255,0.5) 1:#61DDAA'],
                                sizeField='size',
                                size=[5,20],
                                shape='circle',
                                appendPadding=30
                        )
        ],
        style={
            'background': 'white',
            'borderRadius': '4px',
            'height': '100%',
            'padding': '20px'
        }
    )


