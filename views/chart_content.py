from dash import html
import feffery_antd_components as fac

from .chart_components import (
    breadcrumb,hello_word,divider,target_render,line_render,bar_render,pie_render,scatter_render
)

# 内容区
def render_content():
    return html.Div(
        [
            breadcrumb,
            html.Div(
                [
                    hello_word,
                    divider,
                    target_render(),
                    divider,
                    # chart_title(),
                    line_render(),
                ],
                style={
                    'background': 'white',
                    'marginBottom': '16px',
                    'borderRadius': '4px',
                    'padding': '20px'
                }
            ),
            fac.AntdRow(
                [
                    fac.AntdCol(
                        bar_render(),
                        span=12,
                        style={
                            'paddingRight': '10px'
                        }
                    ),
                    fac.AntdCol(
                        pie_render(),
                        span=12,
                        style={
                            'paddingLeft': '10px'
                        }
                    )
                ],
                style={
                    'marginBottom': '16px',
                    'height': '600px'
                }
            ),
            scatter_render(),
            fac.AntdDivider(isDashed=True),
            html.Div(
                fac.AntdText('Design with MangTi'),
                style={
                    'textAlign': 'right',
                    'paddingRight': '20px',
                }
            )
        ],
        style={
            'padding': '25px 20px',
            'background': '#f2f3f5'
        }
    )
