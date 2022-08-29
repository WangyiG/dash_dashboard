
from dash import dcc, html
import feffery_antd_components as fac
import feffery_utils_components as fuc

from config import Config
from server import app, server

from views import layout_components


app.layout = fuc.FefferyTopProgress(
    html.Div(
        [
            # 注入hash路由监听
            dcc.Location(id='url'),

            # 页首
            layout_components.page_start,

            # 侧边菜单+主体内容,使用flex自适应
            fac.AntdRow(
                [
                    # 侧边栏
                    layout_components.side_view,

                    # 图表主体区
                    layout_components.content,

                    # 返回顶部
                    fac.AntdBackTop(
                        duration=0.5
                    )
                ],
                wrap=False
            )
        ]
    ),
    listenPropsMode='exclude',
    excludeProps=Config.exclude_props,
    minimum=0.33,
    speed=800,
    debug=True
)

if __name__ == '__main__':
    app.run(debug=True)
