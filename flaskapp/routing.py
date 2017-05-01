from controllers.index import index
from controllers.api.results import get_results
from controllers.api.counter import get_counter, add_counter
from controllers.api.binary import get_binary, toggle_binary

import main

main.app.add_url_rule('/', 'index', index)
main.app.add_url_rule("/results",'get_results', get_results)
main.app.add_url_rule("/counter",'get_counter', get_counter)
main.app.add_url_rule("/counter/add",'add_counter', add_counter)
main.app.add_url_rule("/binary",'get_binary', get_binary)
main.app.add_url_rule("/binary/toggle",'toggle_binary', toggle_binary)
