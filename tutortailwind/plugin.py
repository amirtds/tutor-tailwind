import pkg_resources

from tutor import hooks

from .__about__ import __version__


################# Configuration
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
        "WELCOME_MESSAGE": "The place for all your online learning",
        "PRIMARY_COLOR": "#3b85ff",  # cool blue
        # Footer links are dictionaries with a "title" and "url"
        # To remove all links, run:
        # tutor config save --set TAILWIND_FOOTER_NAV_LINKS=[] --set TAILWIND_FOOTER_LEGAL_LINKS=[]
        "FOOTER_NAV_LINKS": [
            {"title": "About", "url": "/about"},
            {"title": "Contact", "url": "/contact"},
        ],
        "FOOTER_LEGAL_LINKS": [
            {"title": "Terms of service", "url": "/tos"},
            {
                "title": "Tailwind theme for Open edX",
                "url": "https://github.com/amirtds/tutor-tailwind",
            },
        ],
    },
    "unique": {},
    "overrides": {},
}

# Theme templates
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("tutortailwind", "templates")
)
# This is where the theme is rendered in the openedx build directory
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("tailwind", "build/openedx/themes"),
    ],
)

# Force the rendering of scss files, even though they are included in a "partials" directory
hooks.Filters.ENV_PATTERNS_INCLUDE.add_item(
    r"tailwind/lms/static/sass/partials/lms/theme/"
)

hooks.Filters.ENV_PATCHES.add_items(
    [
        # MFE will install header version 3.0.x and will include indigo-footer as a
        # separate package for use in env.config.jsx
        (
            "mfe-dockerfile-post-npm-install-learning",
            """
RUN npm install '@edx/brand@git+https://github.com/amirtds/brand-openedx.git#370ee526a3c3b921ca43738ea4766e8e536723b5'
RUN npm install '@edx/frontend-component-header@git+https://github.com/amirtds/frontend-component-header#807f38f3d0c6858b79b0db4d7ea22c97a3c30542'
RUN npm install '@edx/frontend-component-footer@git+https://github.com/amirtds/frontend-component-footer#e4ebe43a7f9f9f951640876a3dea8114b5189edb'

""",
        ),
        (
            "mfe-dockerfile-post-npm-install-authn",
            """
RUN npm install '@edx/brand@git+https://github.com/amirtds/brand-openedx.git#370ee526a3c3b921ca43738ea4766e8e536723b5'
""",
        ),
        # Tutor-Indigo v2.1 targets the styling updates in discussions and learner-dashboard MFE
        # brand-openedx is related to styling updates while others are for header and footer updates
        (
            "mfe-dockerfile-post-npm-install-discussions",
            """
RUN npm install '@edx/brand@git+https://github.com/amirtds/brand-openedx.git#370ee526a3c3b921ca43738ea4766e8e536723b5'
RUN npm install '@edx/frontend-component-header@git+https://github.com/amirtds/frontend-component-header#807f38f3d0c6858b79b0db4d7ea22c97a3c30542'
RUN npm install '@edx/frontend-component-footer@git+https://github.com/amirtds/frontend-component-footer#e4ebe43a7f9f9f951640876a3dea8114b5189edb'
""",
        ),
        (
            "mfe-dockerfile-post-npm-install-learner-dashboard",
            """
RUN npm install '@edx/brand@git+https://github.com/amirtds/brand-openedx.git#370ee526a3c3b921ca43738ea4766e8e536723b5'
RUN npm install '@edx/frontend-component-header@git+https://github.com/amirtds/frontend-component-header#807f38f3d0c6858b79b0db4d7ea22c97a3c30542'
RUN npm install '@edx/frontend-component-footer@git+https://github.com/amirtds/frontend-component-footer#e4ebe43a7f9f9f951640876a3dea8114b5189edb'
""",
        ),
        (
            "mfe-dockerfile-post-npm-install-profile",
            """
RUN npm install '@edx/brand@git+https://github.com/amirtds/brand-openedx.git#370ee526a3c3b921ca43738ea4766e8e536723b5'
RUN npm install '@edx/frontend-component-header@git+https://github.com/amirtds/frontend-component-header#807f38f3d0c6858b79b0db4d7ea22c97a3c30542'
RUN npm install '@edx/frontend-component-footer@git+https://github.com/amirtds/frontend-component-footer#e4ebe43a7f9f9f951640876a3dea8114b5189edb'
""",
        ),
        (
            "mfe-dockerfile-post-npm-install-account",
            """
RUN npm install '@edx/brand@git+https://github.com/amirtds/brand-openedx.git#370ee526a3c3b921ca43738ea4766e8e536723b5'
RUN npm install '@edx/frontend-component-header@git+https://github.com/amirtds/frontend-component-header#807f38f3d0c6858b79b0db4d7ea22c97a3c30542'
RUN npm install '@edx/frontend-component-footer@git+https://github.com/amirtds/frontend-component-footer#e4ebe43a7f9f9f951640876a3dea8114b5189edb'
""",
        ),
    ]
)

# Load all configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"TAILWIND_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"TAILWIND_{key}", value) for key, value in config["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config["overrides"].items()))