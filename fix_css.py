import re

with open('/Users/Bec/Dev/qh-design-system/prototypes/logo-lockup-option2.html', 'r') as f:
    content = f.read()

# Remove the CSS that was injected multiple times
css_pattern = r'/\* Option 2 Search Styles \*/.*?\.qld__header__main \.qld__header__brand {\s*padding-bottom: 2rem;\s*}\s*}'

content = re.sub(css_pattern, '', content, flags=re.DOTALL)

# Add it exactly once to the end of the first style block
css = """
    /* Option 2 Search Styles */
    .qld__main-nav__toggle-search { display: none !important; }
    
    @media (max-width: 991px) {
      #qld-header-search {
        display: block !important;
        position: relative;
        padding: 1rem;
        background: #f1f2f2;
        width: 100%;
        box-shadow: none;
        border-bottom: 1px solid #d1d2d2;
      }
      .qld__search-form--wrapper {
        padding: 0;
        margin: 0;
        box-shadow: none;
        background: transparent;
        border: none;
      }
      .qld__search-form__label {
        font-size: 1.25rem;
      }
    }

    @media (min-width: 992px) {
      .qld__main-nav__menu-inner {
        display: flex;
        align-items: center;
        justify-content: space-between;
      }
      .qld__main-nav__menu-list {
        display: flex;
        flex: 1;
      }
      .qld__main-nav__item-link {
        border-bottom: none !important; /* prevent weird borders in flex */
      }
      #qld-header-search {
        display: block !important;
        position: static !important;
        background: transparent !important;
        border: none !important;
        padding: 0 1.5rem !important;
        margin-left: auto;
        width: 320px;
        box-shadow: none !important;
      }
      .qld__search-form--wrapper {
        margin: 0 !important;
        padding: 0 !important;
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
      }
      .qld__search-form__label {
        display: none !important;
      }
      .qld__search-form__inner {
        min-width: unset !important;
        width: 100% !important;
      }
      
      .qld__header__main .qld__header__brand {
        padding-bottom: 2rem;
      }
    }
"""

content = content.replace('</style>', css + '\n  </style>', 1)

with open('/Users/Bec/Dev/qh-design-system/prototypes/logo-lockup-option2.html', 'w') as f:
    f.write(content)
print("Fixed")
