import re

with open('/Users/Bec/Dev/qh-design-system/prototypes/logo-lockup-option2.html', 'r') as f:
    content = f.read()

# Remove the search form from its current location
search_form_match = re.search(r'<div id="qld-header-search" class="qld__header__search">.*?<div class="qld__main-nav__focus-trap-bottom"></div>\s*</div>', content, re.DOTALL)
if search_form_match:
    search_form = search_form_match.group(0)
    content = content.replace(search_form, '')
else:
    print("Could not find search form")
    exit(1)

# Insert it inside qld__main-nav__menu-inner right after the header
insert_point = r'(<div class="\s*qld__main-nav__header qld__main-nav__header--dark\s*">\s*<h2 class="qld__main-nav__menu-heading" tabindex="-1">Menu</h2>\s*<button class="qld__main-nav__toggle qld__main-nav__toggle--close" aria-controls="main-nav">\s*<svg class="qld__icon qld__icon--sm" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">\s*<use href="\.\./dist/mysource_files/img/QLD-icons\.svg#close"></use>\s*</svg>\s*<span class="qld__main-nav__toggle-text">Close</span>\s*</button>\s*</div>)'

if re.search(insert_point, content, re.DOTALL):
    content = re.sub(insert_point, r'\1\n' + search_form.replace('\\', '\\\\'), content, count=1, flags=re.DOTALL)
else:
    print("Could not find insert point")
    exit(1)

# Add CSS
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
content = content.replace('</style>', css + '\n  </style>')

with open('/Users/Bec/Dev/qh-design-system/prototypes/logo-lockup-option2.html', 'w') as f:
    f.write(content)
print("Done")
