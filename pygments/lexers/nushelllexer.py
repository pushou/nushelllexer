import re
from pygments.lexer import Lexer, RegexLexer, do_insertions, bygroups, \
    include, default, this, using, words, line_re
from pygments.token import Punctuation, Whitespace, \
    Text, Comment, Operator, Keyword, Name, String, Number, Generic
from pygments.util import shebang_matches

__all__ = ['NuShellLexer']



class NuShellLexer(RegexLexer):
    name = 'NuShell'
    aliases = ['nushell', 'nu']
    filenames = ['*.nu']
    url = 'https://fr.wikipedia.org/wiki/Nutshell'
    version_added = '0.1'

    tokens = {
        'root': [
            (r'#.*$', Comment.Single),
            (r'(\bdef\b)(\s+)(\w+)', bygroups(Keyword, Text, Name.Function)),
            (r'\b(let|mut|if|else|for|in|while|break|continue|return|match|case|'
             r'default|try|catch|finally|throw|import|export|from|as|with|async|'
             r'await|yield|class|extends|super|this|new|delete|typeof|instanceof|void|of|'
             r'all|ansi|ansi gradient|ansi link|ansi strip|any|append|ast|banner|bits|'
             r'bits and|bits not|bits or|bits rol|bits ror|bits shl|bits shr|bits xor|'
             r'break|bytes|bytes add|bytes at|bytes build|bytes collect|bytes ends-with|'
             r'bytes index-of|bytes length|bytes remove|bytes replace|bytes reverse|'
             r'bytes starts-with|cal|cd|char|chunks|clear|collect|columns|commandline|'
             r'commandline edit|commandline get-cursor|commandline set-cursor|compact|'
             r'complete|config|config env|config nu|config reset|const|continue|cp|'
             r'create_left_prompt|create_right_prompt|date|date format|date humanize|'
             r'date list-timezone|date now|date to-record|date to-table|date to-timezone|'
             r'debug|debug info|debug profile|decode|decode base32|decode base32hex|'
             r'decode base64|decode hex|decode new-base64|def|default|describe|'
             r'detect columns|drop|do|drop column|drop nth|du|each|each while|echo|'
             r'encode|encode base32|encode base32hex|encode base64|encode hex|'
             r'encode new-base64|add|enumerate|error make|every|exec|exit|explain|'
             r'explore|export|export alias|export const|export def|export extern|'
             r'export module|export use|export-env|extern|fill|filter|find|first|flatten|'
             r'fmt|for|format|format date|format duration|format filesize|format pattern|'
             r'from|from csv|from eml|from ics|from ini|from json|from msgpack|'
             r'from msgpackz|from nuon|from ods|from plist|from ssv|from toml|from tsv|'
             r'from url|from vcf|from xlsx|from xml|from yaml|from yml|goto|generate|'
             r'get|glob|grid|group|group-by|hash|hash md5|hash sha256|headers|help|'
             r'help aliases|help commands|help escapes|help externs|help modules|'
             r'help operators|hide|hide-env|histogram|history|history session|http|'
             r'http delete|http get|http head|http options|http patch|http post|http put|'
             r'if|ignore|input|input list|input listen|insert|inspect|interleave|into|'
             r'into binary|into bits|into bool|into cell-path|into datetime|into duration|'
             r'into filesize|into float|into glob|into int|into record|into sqlite|'
             r'into string|into value|is-admin|is-empty|is-not-empty|is-terminal|items|'
             r'join|keybindings|keybindings default|keybindings list|keybindings listen|'
             r'kill|last|length|let|let-env|lines|load-env|loop|ls|match|math|math abs|'
             r'math arccos|math arccosh|math arcsin|math arcsinh|math arctan|math arctanh|'
             r'math avg|math ceil|math cos|math cosh|math exp|math floor|math ln|math log|'
             r'math max|math median|math min|math mode|math product|math round|math sin|'
             r'math sinh|math sqrt|math stddev|math sum|math tan|math tanh|math variance|'
             r'merge|metadata|metadata access|metadata set|mkdir|mktemp|module|move|mut|'
             r'mv|next|nu-check|nu-highlight|open|overlay|overlay hide|overlay list|'
             r'overlay new|overlay use|prev|panic|par-each|parse|path|path basename|'
             r'path dirname|path exists|path expand|path join|path parse|path relative-to|'
             r'path split|path type|plugin|plugin add|plugin list|plugin rm|plugin stop|'
             r'plugin use|polars|polars agg|polars agg-groups|polars all-false|polars all-true|'
             r'polars append|polars arg-max|polars arg-min|polars arg-sort|polars arg-true|'
             r'polars arg-unique|polars arg-where|polars as|polars as-date|polars as-datetime|'
             r'polars cache|polars cast|polars col|polars collect|polars columns|polars concat-str|'
             r'polars contains|polars count|polars count-null|polars cumulative|polars datepart|'
             r'polars decimal|polars drop|polars drop-duplicates|polars drop-nulls|polars dummies|'
             r'polars explode|polars expr-not|polars fetch|polars fill-nan|polars fill-null|'
             r'polars filter|polars filter-with|polars first|polars flatten|polars get|polars get-day|'
             r'polars get-hour|polars get-minute|polars get-month|polars get-nanosecond|'
             r'polars get-ordinal|polars get-second|polars get-week|polars get-weekday|'
             r'polars get-year|polars group-by|polars implode|polars integer|polars into-df|'
             r'polars into-lazy|polars into-nu|polars is-duplicated|polars is-in|polars is-not-null|'
             r'polars is-null|polars is-unique|polars join|polars last|polars lit|polars lowercase|'
             r'polars max|polars mean|polars median|polars min|polars n-unique|polars not|polars open|'
             r'polars otherwise|polars pivot|polars quantile|polars query|polars rename|polars replace|'
             r'polars replace-all|polars reverse|polars rolling|polars sample|polars save|polars schema|'
             r'polars select|polars set|polars set-with-idx|polars shape|polars shift|polars slice|'
             r'polars sort-by|polars std|polars store-get|polars store-ls|polars store-rm|polars str-join|'
             r'polars str-lengths|polars str-slice|polars strftime|polars sum|polars summary|polars take|'
             r'polars unique|polars unpivot|polars uppercase|polars value-counts|polars var|polars when|'
             r'polars with-column|port|port scan|prepend|print|ps|pwd|query|query db|query json|query web|'
             r'query webpage-info|query xml|random|random binary|random bool|random chars|random dice|'
             r'random float|random int|random uuid|range|reduce|reject|rename|return|reverse|rm|roll|'
             r'roll down|roll left|roll right|roll up|rotate|run-external|save|schema|scope|scope aliases|'
             r'scope commands|scope engine-stats|scope externs|scope modules|scope variables|select|seq|'
             r'seq char|seq date|show|shuffle|skip|skip until|skip while|sleep|sort|sort-by|source|'
             r'source-env|split|split cell-path|split chars|split column|split list|split row|split words|'
             r'split-by|start|stor|stor create|stor delete|stor export|stor import|stor insert|stor open|'
             r'stor reset|stor update|str|str camel-case|str capitalize|str contains|str distance|'
             r'str downcase|str ends-with|str expand|str index-of|str join|str kebab-case|str length|'
             r'str pascal-case|str replace|str reverse|str screaming-snake-case|str snake-case|'
             r'str starts-with|str stats|str substring|str title-case|str trim|str upcase|sys|sys cpu|'
             r'sys disks|sys host|sys mem|sys net|sys temp|sys users|table|take|take until|take while|'
             r'tee|term size|timeit|to|to csv|to html|to json|to md|to msgpack|to msgpackz|to nuon|'
             r'to plist|to text|to toml|to tsv|to xml|to yaml|touch|transpose|try|tutor|ulimit|uname|'
             r'uniq|uniq-by|update|update cells|upsert|url|url build-query|url decode|url encode|url join|'
             r'url parse|use|values|version|view|view files|view ir|view source|view span|watch|where|'
             r'which|while|whoami|window|with-env|wrap|zip)\b', Keyword),
            (r'\b(true|false|null|undefined|NaN|Infinity)\b', Keyword.Constant),
            (r'\b(int|float|string|bool|list|dict|table|record|any)\b', Keyword.Type),
            (r'[a-zA-Z_]\w*', Name),
            (r'[-+*/%=<>!&|^~]+', Operator),
            (r'[{}[\]();,.:]', Punctuation),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
            (r'\d+\.\d+', Number.Float),
            (r'\d+', Number.Integer),
            (r'\s+', Text),
        ],
    }

