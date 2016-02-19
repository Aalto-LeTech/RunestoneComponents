# Copyright (C) 2011  Bradley N. Miller
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
__author__ = 'isaacdontjelindell'

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive


DISQUS_COMMENTS = """\
<div id="disqus_thread"></div>
<script>
    var disqus_path = window.location.protocol + '//' + window.location.host + window.location.pathname;
    var disqus_id = '%(identifier)s_' + eBookConfig.course;

    var disqus_config = function () {
        this.page.url = disqus_path;
        this.page.identifier = disqus_id;
    };

    (function() {
        var d = document, s = d.createElement('script');

        s.src = '//%(shortname)s.disqus.com/embed.js';

        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
"""

def setup(app):
    app.add_directive('disqus', DisqusDirective)

    app.add_node(DisqusNode, html=(visit_disqus_node, depart_disqus_node))
    app.connect('doctree-resolved' ,process_disqus_nodes)
    app.connect('env-purge-doc', purge_disqus_nodes)



class DisqusNode(nodes.General, nodes.Element):
    def __init__(self,content):
        super(DisqusNode,self).__init__()
        self.disqus_components = content

def visit_disqus_node(self, node):
    should_render = str(node.document.settings.env.config.html_context["render_disqus"]).lower()
    if should_render == 'true':
        res = DISQUS_COMMENTS
        res = res % node.disqus_components
        self.body.append(res)

def depart_disqus_node(self,node):
    pass

def process_disqus_nodes(app, env, docname):
    pass

def purge_disqus_nodes(app, env, docname):
    pass




class DisqusDirective(Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = False
    option_spec = {'shortname':directives.unchanged_required,
                   'identifier':directives.unchanged_required
                  }


    def run(self):
        """
        generate html to include Disqus box.
        :param self:
        :return:
        """

        return [DisqusNode(self.options)]
