from regparser import plugins

META = {}

#   All current, US CFR titles
CFR_TITLES = [
    None,
    "General Provisions",
    "Grants and Agreements",
    "The President",
    "Accounts",
    "Administrative Personnel",
    "Domestic Security",
    "Agriculture",
    "Aliens and Nationality",
    "Animals and Animal Products",
    "Energy",
    "Federal Elections",
    "Banks and Banking",
    "Business Credit and Assistance",
    "Aeronautics and Space",
    "Commerce and Foreign Trade",
    "Commercial Practices",
    "Commodity and Securities Exchanges",
    "Conservation of Power and Water Resources",
    "Customs Duties",
    "Employees' Benefits",
    "Food and Drugs",
    "Foreign Relations",
    "Highways",
    "Housing and Urban Development",
    "Indians",
    "Internal Revenue",
    "Alcohol, Tobacco Products and Firearms",
    "Judicial Administration",
    "Labor",
    "Mineral Resources",
    "Money and Finance: Treasury",
    "National Defense",
    "Navigation and Navigable Waters",
    "Education",
    "Panama Canal [Reserved]",
    "Parks, Forests, and Public Property",
    "Patents, Trademarks, and Copyrights",
    "Pensions, Bonuses, and Veterans' Relief",
    "Postal Service",
    "Protection of Environment",
    "Public Contracts and Property Management",
    "Public Health",
    "Public Lands: Interior",
    "Emergency Management and Assistance",
    "Public Welfare",
    "Shipping",
    "Telecommunication",
    "Federal Acquisition Regulations System",
    "Transportation",
    "Wildlife and Fisheries",
]

DEFAULT_IMAGE_URL = (
    'https://s3.amazonaws.com/images.federalregister.gov/' +
    '%s/original.gif')

# dict: string->[string]: List of phrases which shouldn't contain defined
# terms. Keyed by CFR part or 'ALL'.
IGNORE_DEFINITIONS_IN = plugins.update_dictionary(
    "eregs_ns.parser.term_ignores", {'ALL': []})

# dict: string->[(string,string)]: List of phrases which *should* trigger a
# definition. Pair is of the form (term, context), where "context" refers to a
# substring match for a specific paragraph. e.g.
# ("bob", "text noting that it defines bob")
INCLUDE_DEFINITIONS_IN = plugins.update_dictionary(
    "eregs_ns.parser.term_definitions", {'ALL': []})

# list of modules implementing the __contains__ and __getitem__ methods
OVERRIDES_SOURCES = [
    'regcontent.overrides'
]

# list of iterable[(xpath, replacement-xml)] modules, which will be loaded
# in regparser.content.Macros
MACROS_SOURCES = [
    'regcontent.macros'
]

# In some cases, it is beneficial to tweak the XML the Federal Register
# provides. This setting specifies file paths to look through for local
# versions of their XML. See also XML_REPO below, which is effectively tacked
# on to the end of this list
LOCAL_XML_PATHS = []


# Sometimes appendices provide examples or model forms that include
# labels that we would otherwise recognize as structural to the appendix
# text itself. This specifies those labels to ignore by regulation
# number, appendix, and label.
APPENDIX_IGNORE_SUBHEADER_LABEL = {}

# Refer to a shared collection of modified FR notices
XML_REPO_PREFIX = 'https://raw.githubusercontent.com/eregs/fr-notices/master/'

# A dictionary of agency-specific external citations
# @todo - move ATF citations to an extension
CUSTOM_CITATIONS = {
    "ATF I 5300.1": "https://atf-eregs.apps.cloud.gov/static/atf_eregs/5300_1.pdf",
    "ATF I 5300.2": "https://www.atf.gov/file/58806/download"}

# PREPROCESSORS = plugins.extend_list('eregs_ns.parser.preprocessors', [
#     "regparser.tree.xml_parser.preprocessors.MoveLastAMDPar",
#     "regparser.tree.xml_parser.preprocessors.SupplementAMDPar",
#     "regparser.tree.xml_parser.preprocessors.ParenthesesCleanup",
#     "regparser.tree.xml_parser.preprocessors.MoveAdjoiningChars",
#     "regparser.tree.xml_parser.preprocessors.ApprovalsFP",
#     "regparser.tree.xml_parser.preprocessors.ExtractTags",
#     "regparser.tree.xml_parser.preprocessors.Footnotes",
#     "regparser.tree.xml_parser.preprocessors.ParseAMDPARs",
#     "regparser.tree.xml_parser.preprocessors.AtfI50032",
#     "regparser.tree.xml_parser.preprocessors.AtfI50031",
#     "regparser.tree.xml_parser.preprocessors.ImportCategories",
#     "regparser.tree.xml_parser.preprocessors.MoveSubpart",
# ])

## Which layers are to be generated, keyed by document type. The ALL key is
## special; layers in this category automatically apply to all document types
# LAYERS = {
#     'cfr': [
#         'regparser.layer.meta.Meta',
#         'regparser.layer.internal_citations.InternalCitationParser',
#         'regparser.layer.table_of_contents.TableOfContentsLayer',
#         'regparser.layer.terms.Terms',
#         'regparser.layer.paragraph_markers.ParagraphMarkers',
#         'regparser.layer.key_terms.KeyTerms',
#         # CFPB specific -- these should be moved to plugins
#         'regparser.layer.interpretations.Interpretations',
#         # SectionBySection layer is a created via a separate command
#     ],
#     'preamble': [
#         'regparser.layer.preamble.key_terms.KeyTerms',
#         'regparser.layer.preamble.internal_citations.InternalCitations',
#         'regparser.layer.preamble.paragraph_markers.ParagraphMarkers'
#     ],
#     # It probably makes more sense to use plugins.update_dictionary, but we're
#     # keeping this for backwards compatibility
#     'ALL': plugins.extend_list('eregs_ns.parser.layers', [
#         'regparser.layer.external_citations.ExternalCitationParser',
#         'regparser.layer.formatting.Formatting',
#         'regparser.layer.graphics.Graphics',
#     ]),
# }

# Regulations.gov settings. The demo key is rate limited by IP; sign up for
# your own key at
# http://regulationsgov.github.io/developers/key/
REGS_GOV_API = 'https://api.data.gov/regulations/v3/'
REGS_GOV_KEY = 'DEMO_KEY'

# These are the host and port for the regparser Django server running the
# administrative UI.
# It's apparently necessary to include the hostname and post in settings
# because the information in the HTTP request can be spoofed.
# For development, override these in ``local_settings.py``.
CANONICAL_HOSTNAME = "https://example.com"
CANONICAL_PORT = ""

# The URL for the regulations-site API that parser commands invoked from the
# web API/UI should run against:
EREGS_SITE_API_URL = "http://localhost:1234/api/"

try:
    from local_settings import *
except ImportError:
    pass
