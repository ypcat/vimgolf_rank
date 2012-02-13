from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def index (challenges):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<!DOCTYPE HTML>\n'])
    extend_([u'<html>\n'])
    extend_([u'\n'])
    extend_([u'<head>\n'])
    extend_([u'    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n'])
    extend_([u'    <title>VimGolf Ranking</title>\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" href="css/main.css" />\n'])
    extend_([u'</head>\n'])
    extend_([u'\n'])
    extend_([u'<body id="home">\n'])
    extend_([u'\n'])
    extend_([u'    <header>\n'])
    extend_([u'        <h3><b>Open VimGolf Challenges</b></h3>\n'])
    extend_([u'    </header>\n'])
    extend_([u'\n'])
    extend_([u'    <section>\n'])
    extend_([u'        <h4><a href="/top">Leaderboard</a></h4>\n'])
    extend_([u'        <div>\n'])
    for c in loop.setup(challenges):
        extend_(['        ', u'<div>\n'])
        extend_(['        ', u'    <a href="challenges/', escape_((c.handle), True), u'">', escape_((c.title), True), u'</a>\n'])
        extend_(['        ', u'    - ', escape_((len(c.active_golfers)), True), u' active golfers\n'])
        extend_(['        ', u'</div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </section>\n'])
    extend_([u'\n'])
    extend_([u'    <script type="text/javascript" src="/js/main.js"></script>\n'])
    extend_([u'\n'])
    extend_([u'</body>\n'])
    extend_([u'\n'])
    extend_([u'</html>\n'])
    extend_([u'\n'])

    return self

index = CompiledTemplate(index, 'templates/index.html')
join_ = index._join; escape_ = index._escape

