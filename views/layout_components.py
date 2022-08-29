
from dash import dcc, html
import feffery_antd_components as fac
from server import app
from config import Config
from dash.dependencies import Input, Output, State
from urllib import parse
from views import chart_content


# 页首
page_start = fac.AntdRow(
                [
                    fac.AntdCol(
                        html.Img(
                            src= app.get_asset_url('imgs/re-data.svg'),
                            style={
                                'height': '40px',
                                'padding': '0 0px',
                                'margin': '7px 10px 0 15px'
                            }
                        ),
                    ),
                    fac.AntdCol(
                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    "Dashboard Demo",
                                    strong=True,
                                    style={
                                        'fontSize': '35px'
                                    }
                                )
                            ]
                        )
                    )
                ],
                align="middle",
                style={
                    'height': '64px',
                    'boxShadow': 'rgb(240 241 242) 0px 2px 14px',
                    'background': 'white',
                    'marginBottom': '5px'
                }
            )



# 带侧边栏收缩回调的侧边栏
side_view=fac.AntdCol(
                        fac.AntdAffix(
                            html.Div(
                                [
                                    fac.AntdMenu(
                                        id='router-menu',
                                        menuItems=Config.menuItems,
                                        mode='inline',
                                        defaultOpenKeys=[
                                            'dashboard', 'other-pages'
                                        ],
                                        style={
                                            'height': '100%',
                                            'overflow': 'hidden auto',
                                            'paddingBottom': '50px'
                                        }
                                    ),

                                    fac.AntdButton(
                                        fac.AntdIcon(
                                            id='fold-side-menu-icon',
                                            icon='antd-arrow-left'
                                        ),
                                        id='fold-side-menu',
                                        type='text',
                                        shape='circle',
                                        style={
                                            'position': 'absolute',
                                            'zIndex': 999,
                                            'top': '10px',
                                            'right': '-15px',
                                            'boxShadow': '0 4px 10px 0 rgba(0,0,0,.1)',
                                            'background': 'white'
                                        }
                                    )
                                ],
                                id='side-menu',
                                style={
                                    'width': '250px',
                                    'height': '100vh',
                                    'overflowY': 'auto',
                                    'transition': 'width 0.2s',
                                    'borderRight': '1px solid rgb(240, 240, 240)',
                                    'paddingRight': 20,
                                    'boxShadow': '0 2px 5px 0 rgb(0 0 0 / 8%)'
                                }
                            ),
                            offsetTop=0
                        ),
                        flex='none'
                    )



app.clientside_callback(
    '''
    (nClicks, oldStyle) => {
        if (nClicks) {
            if (oldStyle.width === '250px') {
                return [
                    {
                        'width': 20,
                        'height': '100vh',
                        'overflowY': 'auto',
                        'transition': 'width 0.2s',
                        'borderRight': '1px solid rgb(240, 240, 240)',
                        'paddingRight': 20
                    },
                    'antd-arrow-right'
                ]
            }
            return [
                {
                    'width': '250px',
                    'height': '100vh',
                    'transition': 'width 0.2s',
                    'borderRight': '1px solid rgb(240, 240, 240)',
                    'paddingRight': 20
                },
                'antd-arrow-left'
            ]
        }
        return window.dash_clientside.no_update;
    }
    ''',
    [
        Output('side-menu', 'style'),
        Output('fold-side-menu-icon', 'icon')
    ],
    Input('fold-side-menu', 'nClicks'),
    State('side-menu', 'style')
)



# 带路由回调的图表主体
content =  fac.AntdCol(
                        [
                            html.Div(
                                id='docs-content',
                                style={
                                    'backgroundColor': 'rgb(255, 255, 255)'
                                }
                            )
                        ],
                        flex='auto'
                    )

@app.callback(
    [
        Output('docs-content', 'children'),
        Output('router-menu', 'currentKey')
    ],
    Input('url', 'hash'),
    State('url', 'pathname')
)
def render_content(hash_, pathname):
    '''
    路由回调
    '''

    if pathname == '/':
        if parse.unquote(hash_) == '#概览面板' or not hash_:
            
            return chart_content.render_content(), '/#概览面板'

        return fac.AntdResult(status='info', title='示例页面'), '/'+hash_

    return fac.AntdResult(status='404', title='您访问的页面不存在！'), pathname
