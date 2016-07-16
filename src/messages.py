import config


message = {
    'tabs': 'Tabs are not needed',
    'line_limit': 'This line is above the recommended line limit of ' +
                   str(config.line_limit) + ' columns',
    'lonely_parenthesis': 'Parenthesis should never be on their own line',
    'blank_line': 'There should be a blank line between each procedure definiton',
    'bad_variable': 'Badly named variable. Variables should be dash-separated'
}
