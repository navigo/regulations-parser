import logging

import click

from regparser.history.versions import Version
from regparser.index import entry
from regparser.notice.xml import NoticeXML
from regparser.tree.xml_parser.reg_text import build_tree


logger = logging.getLogger(__name__)


def regtext_for_part(notice_xml, cfr_title, cfr_part):
    """Filter to only the REGTEXT in question"""
    xpath = './/REGTEXT[@TITLE={} and @PART={}]'.format(cfr_title, cfr_part)
    matches = notice_xml.xpath(xpath)
    if not matches:
        logger.warning('No matching REGTEXT in this file')
    else:
        if len(matches) > 1:
            logger.warning('Multiple matching REGTEXTs; using the first')
        return matches[0]


def process_xml(notice_xml, cfr_title, cfr_part, version_id):
    """Parse tree from XML and write the relevant index entries"""
    notice_xml.derive_where_needed()
    version = Version(identifier=version_id, effective=notice_xml.effective,
                      published=notice_xml.published)
    tree = build_tree(regtext_for_part(notice_xml, cfr_title, cfr_part))

    entry.FinalVersion(cfr_title, cfr_part, version_id).write(version)
    entry.Tree(cfr_title, cfr_part, version_id).write(tree)
    entry.Notice(version_id).write(notice_xml)


@click.command()
@click.argument('cfr_title', type=int)
@click.argument('cfr_part', type=int)
@click.argument('version', type=str)
@click.argument('xml_file_path', type=click.Path(exists=True))
def full_issuance(cfr_title, cfr_part, version, xml_file_path):
    """Import the provided XML into a regulation tree, version, and notice."""
    with open(xml_file_path, 'rb') as f:
        notice_xml = NoticeXML(f.read(), xml_file_path)
    process_xml(notice_xml, cfr_title, cfr_part, version)
