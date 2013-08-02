#vim: set encoding=utf-8
from unittest import TestCase

from regparser.tree.struct import Node, NodeEncoder
from regparser.tree.build import *

class TreeBuildTest(TestCase):

    def test_find_cfr_part(self):
        text = "Some text here\n"
        text += "This has 201.44 in it. But also 203.33\n"
        text += "But then, 201.33 returns."

        self.assertEqual(201, find_cfr_part(text))

    def test_build_whole_regtree(self):
        """Integration test for the plain-text regulation tree parser"""
        text = "Regulation Q\n"
        text += u"§ 200.1 First section.\n"
        text += "(a) First par\n"
        text += "(b) Second par\n"
        text += u"§ 200.2 Second section.\n"
        text += "Content without sub pars\n"
        text += "Appendix A to Part 200 - Appendix Title\n"
        text += "A-1 Appendix 1\n"
        text += "(a) Appendix par 1\n"
        text += "Supplement I to Part 200 - Official Interpretations\n"
        text += "Section 200.2 Second section\n"
        text += "2(a)(5) First par\n"
        text += "1. Commentary 1\n"
        text += "2. Commentary 2\n"

        node201 = Node("\n", label=['200', '1'], 
            title=u"§ 200.1 First section.", children=[
                Node(u"(a) First par\n", label=["200","1","a"]),
                Node(u"(b) Second par\n", label=["200","1","b"])
            ]
        )
        node202 = Node("\nContent without sub pars\n", label=["200","2"], 
            title=u"§ 200.2 Second section.")
        nodeA = Node("\n", label=["200","A"], node_type=Node.APPENDIX,
            title="Appendix A to Part 200 - Appendix Title", children=[
                Node("\n", label=["200","A","1"], title="A-1 Appendix 1",
                    node_type=Node.APPENDIX,
                    children=[Node("(a) Appendix par 1\n", 
                        node_type=Node.APPENDIX, label=["200","A","1","a"])])
            ]
        )
        nodeI = Node('\n', label=['200', 'Interp'], node_type=Node.INTERP,
            title='Supplement I to Part 200 - Official Interpretations',
            children=[
                Node('\n', label=['200', '2', 'Interp'], node_type=Node.INTERP,
                    title='Section 200.2 Second section'),
                Node('\n', label=['200','2','a','5','Interp'],
                    node_type=Node.INTERP, title='2(a)(5) First par',
                    children=[
                        Node('1. Commentary 1\n', node_type=Node.INTERP,
                            label=['200', '2', 'a', '5', 'Interp', '1']),
                        Node('2. Commentary 2\n', node_type=Node.INTERP,
                            label=['200', '2', 'a', '5', 'Interp', '2'])
                    ]
                )
            ]
        )
        res = build_whole_regtree(text)
        #   Convert to JSON so we can ignore some unicode issues
        enc = NodeEncoder(sort_keys=True)
        self.assertEqual(
            enc.encode(build_whole_regtree(text)), 
            enc.encode(Node("\n", label=["200"], title="Regulation Q", 
                children=[ node201, node202, nodeA, nodeI ]))
        )
