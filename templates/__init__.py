from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def challenges (challenge):
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
    extend_([u'        <h3><a href="http://vimgolf.com/challenges/', escape_((challenge.handle), True), u'"><b>', escape_((challenge.title), True), u'</b></a></h3>\n'])
    extend_([u'    </header>\n'])
    extend_([u'\n'])
    extend_([u'    <section>\n'])
    extend_([u'        <h5>Leaderboard</h5>\n'])
    extend_([u'        <div>\n'])
    for golfer in loop.setup(challenge.active_golfers):
        extend_(['        ', u'<div>#', escape_((loop.index), True), u' - <a href="/', escape_(golfer, True), u'">', escape_(golfer, True), u'</a></div>\n'])
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

challenges = CompiledTemplate(challenges, 'templates\\challenges.html')
join_ = challenges._join; escape_ = challenges._escape

# coding: utf-8
def global_ranks (golfers, date):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<!DOCTYPE HTML>\n'])
    extend_([u'<html>\n'])
    extend_([u'\n'])
    extend_([u'<head>\n'])
    extend_([u'    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n'])
    extend_([u'    <title>VimGolf Rankings</title>\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" href="css/main.css" />\n'])
    extend_([u'</head>\n'])
    extend_([u'\n'])
    extend_([u'<body id="home">\n'])
    extend_([u'    <header>\n'])
    extend_([u'    <h3>Complete <a href="http://vimgolf.com">VimGolf</a> Rankings</h3>\n'])
    extend_([u'    </header>\n'])
    extend_([u'    <div>\n'])
    extend_([u'        <p>Here is the official definition of rankings:</p>\n'])
    extend_([u'        <ul>\n'])
    extend_([u'            <li>Global rank is the sum of your ranks on each challenge</li>\n'])
    extend_([u'            <li>Skipping a challenge implicitly yields the lowest rank</li>\n'])
    extend_([u'        </ul>\n'])
    extend_([u'        <p>Created on ', escape_(date, True), u' by jyunfan@gmail.com and ypcat6@gmail.com</p>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <section>\n'])
    extend_([u'    <table>\n'])
    extend_([u'        <tr class="topheader"><td>Ranking</td><td>ID</td><td>Global Rank</td></tr>\n'])
    for g in loop.setup(golfers):
        extend_(['        ', u'<tr class="top">\n'])
        extend_(['        ', u'    <td class="rank">', escape_((g.rank), True), u'</td>\n'])
        extend_(['        ', u'    <td><a href="http://vimgolf.com/', escape_((g.handle), True), u'" class="top">', escape_((g.handle), True), u'</a></td>\n'])
        extend_(['        ', u'    <td class="global_rank">', escape_((g.global_rank), True), u'</td>\n'])
        extend_(['        ', u'</tr>\n'])
    extend_([u'    </table> \n'])
    extend_([u'    </section>\n'])
    extend_([u'\n'])
    extend_([u'    <footer>\n'])
    extend_([u'        <p>\n'])
    extend_([u'        </p>\n'])
    extend_([u'    </footer>\n'])
    extend_([u'\n'])
    extend_([u'    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>\n'])
    extend_([u'    <script type="text/javascript" src="js/main.js"></script>\n'])
    extend_([u'    <script type="text/javascript">\n'])
    extend_([u'        beautify_globalrank();\n'])
    extend_([u'    </script>\n'])
    extend_([u'</body>\n'])
    extend_([u'\n'])
    extend_([u'</html>\n'])
    extend_([u'\n'])

    return self

global_ranks = CompiledTemplate(global_ranks, 'templates\\global_ranks.html')
join_ = global_ranks._join; escape_ = global_ranks._escape

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
    extend_([u'    <footer>\n'])
    extend_([u'        <p>\n'])
    extend_([u'            Install <a href="/js/vimgolf_rank.user.js">vimgolf-rank</a>\n'])
    extend_([u'            greasemonkey script to enable more information on vimgolf.com\n'])
    extend_([u'        </p>\n'])
    extend_([u'    </footer>\n'])
    extend_([u'\n'])
    extend_([u'    <script type="text/javascript" src="/js/main.js"></script>\n'])
    extend_([u'\n'])
    extend_([u'</body>\n'])
    extend_([u'\n'])
    extend_([u'</html>\n'])
    extend_([u'\n'])

    return self

index = CompiledTemplate(index, 'templates\\index.html')
join_ = index._join; escape_ = index._escape

