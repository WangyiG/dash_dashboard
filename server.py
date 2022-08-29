import dash

app = dash.Dash(
    __name__,

    # 忽略在交互后才产生的组件的扫描匹配错误
    suppress_callback_exceptions=True,
    update_title=None,

    # assets中静态文件等会加载到网络,压缩后有助于回调
    compress=True
)

# 网页标签头图标与文本内容
app._favicon = 'favicon.ico'
app.title = " MT's Dashboard Demo "

# 部署用服务接口
server = app.server
