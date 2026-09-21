import re

with open('/Users/Bec/Dev/qh-design-system/prototypes/logo-lockup-govuk.html', 'r') as f:
    content = f.read()

# Replace the entire <header> and <nav id="mainmenu"> with our new structure
header_pattern = r'<header class="qld__header" role="banner">.*?</nav>'
new_header_html = """<header class="qld__header qld__header--govuk" role="banner">
    <div class="qld__header__main qld__header__main--dark">
      <div class="container-fluid qld__header__govuk-container">
        
        <div class="qld__header__brand qld__header__govuk-brand">
          <a href="https://www.qld.gov.au" class="qld__header__govuk-logo">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 331 56" fill="currentColor" height="32" aria-label="Queensland Government">
              <path d="M129.5 28c0-3 1.7-4.4 3.7-4.4s3.7 1.4 3.7 4.4v9h-7.4v-9zm25.8 4c0 3.3-1.8 5.7-4.6 5.7s-4.6-2.4-4.6-5.7v-8.8h-7.7v9.4c0 7 5 11.2 12.3 11.2 7.2 0 12.3-4.1 12.3-11v-9.6h-7.7v8.8zm-16-11.7c-5.8 0-9.6 4-10.7 9h7.3c.7-1.5 2-2.3 3.6-2.3s2.9 1 2.9 2.7v.5c-7 .7-13.6 2-13.6 8.5 0 4.3 3 7.3 7.3 7.3 3.5 0 6.6-1.9 8.2-5v4.5h7.3V31c0-6-3.8-10.7-12.3-10.7zm3.1 15.6c0 1.6-1.2 2.6-2.7 2.6-1.5 0-2.5-1-2.5-2.5 0-2 2-3 6.3-3.7l-.1 3.4-.1.2h-.9zm32.8-15.6c-7.6 0-13.3 5.7-13.3 13.2S167.6 44 175.2 44s13.4-5.7 13.4-13.2-5.7-12.9-13.4-12.9zm0 19c-3.3 0-5.6-2.5-5.6-6.1s2.2-6 5.6-6 5.6 2.5 5.6 6-2.3 6.1-5.6 6.1zm22.4-19c-5.3 0-8.9 2.5-10.3 6.6h7.3c.8-1.5 2-2.1 3.5-2.1 1.7 0 2.5 1 2.5 2.5v.3c-1.3 0-2.7.1-4.2.3-4.5.6-8.2 2-8.2 7.6 0 4.2 2.7 7 6.7 7 3.2 0 6-1.9 7.4-4.8v4.3h7.4v-11c0-5.8-4-10.7-12.1-10.7zm3 14.8c0 2.1-1.6 3.4-3.5 3.4-1.6 0-2.7-.9-2.7-2.3 0-1.8 1.6-2.5 4.5-2.9l1.7-.2v2zm30.3-8h-6.8c-.5-3.3-2.6-5.1-5.6-5.1-3 0-5 2.1-5 5.2 0 3 1.9 4.8 5.6 5.7l2.8.7c5.8 1.4 8.7 4.1 8.7 9.8 0 6-4.5 10.6-11.4 10.6-7.2 0-11.7-4.4-12.3-11.1h7.5c.6 3.3 2.6 5 5.5 5 3.1 0 5-2 5-5.2 0-3.3-2-4.9-5.9-5.8l-2.6-.6c-5.3-1.3-8.4-4.3-8.4-9.6 0-5.8 4.6-10.5 11.2-10.5 6.6.1 11 4.1 11.7 10.9zm24.6 4.7h-11.8v2c0 2.2 1.5 3.6 3.6 3.6s3.1-1.2 3.6-3h7.3c-.6 4.8-4.5 8.1-10.8 8.1-7.2 0-11.4-5.2-11.4-12.9s4.6-13 11.6-13c7.2 0 11.3 5.4 11.3 12.5v2.7zm-7.6-3.8c-.2-1.9-1.5-3.2-3.4-3.2-2 0-3.4 1.3-3.8 3.2h7.2zm30.5 11.1c-1.4 1.7-3.6 2.8-6.1 2.8-4.7 0-7.8-3.3-7.8-8.5V20.8h-7.6V43h7.5v-4.4c1.7 3.3 4.8 5.3 8.7 5.3 3.6 0 6.6-1.5 8.3-4.2V43h7.5V20.8h-7.6v11.7c0 2 0 3.2-.2 5.1l-2.7 5.4zm-6.2-7.8c0 2.9-1.5 4.7-3.8 4.7s-3.7-1.8-3.7-4.7v-9.3h7.5v9.3zM85.4 19.3c5.3 0 8.9-2.5 10.3-6.6h-7.3c-.8 1.5-2 2.1-3.5 2.1-1.7 0-2.5-1-2.5-2.5v-.3c1.3 0 2.7-.1 4.2-.3 4.5-.6 8.2-2 8.2-7.6 0-4.2-2.7-7-6.7-7-3.2 0-6 1.9-7.4 4.8V-2.4h-7.4v11C73.3 14.4 77.3 19.3 85.4 19.3zm-3-14.8c0-2.1 1.6-3.4 3.5-3.4 1.6 0 2.7.9 2.7 2.3 0 1.8-1.6 2.5-4.5 2.9l-1.7.2v-2zM45 44h8.3L40.2 11.8H31L17.8 44h8.5l2.4-6.3h13.9L45 44zm-14.1-13l4.7-12.7L40.2 31h-9.3zm59.2 13h7.5V18.1h-7.5V44zm-6.9-4.8c-1.4 1.7-3.6 2.8-6.1 2.8-4.7 0-7.8-3.3-7.8-8.5V20.8h-7.6V43h7.5v-4.4c1.7 3.3 4.8 5.3 8.7 5.3 3.6 0 6.6-1.5 8.3-4.2V43h7.5V20.8h-7.6v11.7c0 2 0 3.2-.2 5.1l-2.7 5.4zm-6.2-7.8c0 2.9-1.5 4.7-3.8 4.7s-3.7-1.8-3.7-4.7v-9.3h7.5v9.3zm57.2 4.4h-6.8c-.5-3.3-2.6-5.1-5.6-5.1-3 0-5 2.1-5 5.2 0 3 1.9 4.8 5.6 5.7l2.8.7c5.8 1.4 8.7 4.1 8.7 9.8 0 6-4.5 10.6-11.4 10.6-7.2 0-11.7-4.4-12.3-11.1h7.5c.6 3.3 2.6 5 5.5 5 3.1 0 5-2 5-5.2 0-3.3-2-4.9-5.9-5.8l-2.6-.6c-5.3-1.3-8.4-4.3-8.4-9.6 0-5.8 4.6-10.5 11.2-10.5 6.6.1 11 4.1 11.7 10.9zM203 27h-6.8c-.5-3.3-2.6-5.1-5.6-5.1-3 0-5 2.1-5 5.2 0 3 1.9 4.8 5.6 5.7l2.8.7c5.8 1.4 8.7 4.1 8.7 9.8 0 6-4.5 10.6-11.4 10.6-7.2 0-11.7-4.4-12.3-11.1h7.5c.6 3.3 2.6 5 5.5 5 3.1 0 5-2 5-5.2 0-3.3-2-4.9-5.9-5.8l-2.6-.6c-5.3-1.3-8.4-4.3-8.4-9.6 0-5.8 4.6-10.5 11.2-10.5 6.6.1 11 4.1 11.7 10.9zm24.6 4.7h-11.8v2c0 2.2 1.5 3.6 3.6 3.6s3.1-1.2 3.6-3h7.3c-.6 4.8-4.5 8.1-10.8 8.1-7.2 0-11.4-5.2-11.4-12.9s4.6-13 11.6-13c7.2 0 11.3 5.4 11.3 12.5v2.7zm-7.6-3.8c-.2-1.9-1.5-3.2-3.4-3.2-2 0-3.4 1.3-3.8 3.2h7.2zm30.3-4.2V18h-7.6v26.1h7.6v-3.7c1.3 2.6 3.9 3.5 6.6 3.5 6.7 0 11.4-5.3 11.4-13s-4.6-13.2-11.2-13.2c-2.7 0-5.1.7-6.8 3v-7h0zm2.9 14.1c0-2.8 1.6-4.8 4-4.8s4 2 4 4.8-1.5 4.8-4 4.8-4-2-4-4.8zm37.2-1.1h-11.8v2c0 2.2 1.5 3.6 3.6 3.6s3.1-1.2 3.6-3h7.3c-.6 4.8-4.5 8.1-10.8 8.1-7.2 0-11.4-5.2-11.4-12.9s4.6-13 11.6-13c7.2 0 11.3 5.4 11.3 12.5v2.7zm-7.6-3.8c-.2-1.9-1.5-3.2-3.4-3.2-2 0-3.4 1.3-3.8 3.2h7.2zm20.3-9c-2.2 0-4.3 1.1-5.5 3V20.8h-7.6V43h7.6V30c0-2.5 1.5-3.9 3.8-3.9 1.9 0 3 1 3.5 2.5l7.1-1.2c-1.3-4.6-5.1-6.7-8.9-6.7zM6.5 56h315V0H6.5v56zm32.8-38.3h-7.5V43h7.5V17.7z"></path>
              <path d="M11 25.1c0 5 4.1 9.2 9.2 9.2 5 0 9.2-4.1 9.2-9.2s-4.1-9.2-9.2-9.2c-5 0-9.2 4.1-9.2 9.2z" fill="#000"></path>
            </svg>
          </a>
          <a href="logo-lockup-subsite.html" class="qld__header__govuk-site-name" aria-label="Disaster management homepage">
            Department of Natural Disasters
          </a>
        </div>
        
        <div class="qld__header__govuk-actions">
          <!-- Desktop Search -->
          <div class="qld__header__govuk-search">
            <form action="/search" method="get" role="search" class="qld__header__govuk-search-form">
              <label for="search-input-govuk" class="qld__sr-only">Search</label>
              <input type="search" id="search-input-govuk" name="query" class="qld__header__govuk-search-input" placeholder="Search" autocomplete="off">
              <button type="submit" class="qld__header__govuk-search-button" aria-label="Search">
                <svg class="qld__icon" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                  <use href="../dist/mysource_files/img/QLD-icons.svg#search"></use>
                </svg>
              </button>
            </form>
          </div>
          
          <!-- Menu Toggle -->
          <button id="govuk-menu-toggle" class="qld__header__govuk-menu-toggle" aria-expanded="false" aria-controls="govuk-mega-menu">
            <span class="qld__header__govuk-menu-text">Menu</span>
            <svg class="qld__icon qld__header__govuk-menu-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
              <use href="../dist/mysource_files/img/QLD-icons.svg#menu"></use>
            </svg>
            <svg class="qld__icon qld__header__govuk-close-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" style="display:none;">
              <use href="../dist/mysource_files/img/QLD-icons.svg#close"></use>
            </svg>
          </button>
          
          <!-- Mobile Search Toggle -->
          <button id="govuk-search-toggle" class="qld__header__govuk-search-toggle" aria-expanded="false" aria-controls="govuk-mobile-search">
            <span class="qld__sr-only">Search</span>
            <svg class="qld__icon qld__header__govuk-search-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
              <use href="../dist/mysource_files/img/QLD-icons.svg#search"></use>
            </svg>
            <svg class="qld__icon qld__header__govuk-search-close-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" style="display:none;">
              <use href="../dist/mysource_files/img/QLD-icons.svg#close"></use>
            </svg>
          </button>
        </div>
      </div>
    </div>
    
    <!-- Mobile Search Pane -->
    <div id="govuk-mobile-search" class="qld__header__govuk-mobile-search-pane" style="display: none;">
      <div class="container-fluid">
        <form action="/search" method="get" role="search" class="qld__header__govuk-search-form">
          <label for="search-input-govuk-mobile" class="qld__sr-only">Search</label>
          <input type="search" id="search-input-govuk-mobile" name="query" class="qld__header__govuk-search-input" placeholder="Search" autocomplete="off">
          <button type="submit" class="qld__header__govuk-search-button" aria-label="Search">
            <svg class="qld__icon" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
              <use href="../dist/mysource_files/img/QLD-icons.svg#search"></use>
            </svg>
          </button>
        </form>
      </div>
    </div>
  </header>

  <!-- GOV.UK Style Mega Menu -->
  <nav id="govuk-mega-menu" class="qld__header__govuk-mega-menu" style="display: none;" aria-label="Main navigation">
    <div class="container-fluid">
      <div class="row">
        <div class="col-xs-12 col-md-8">
          <h2 class="qld__header__govuk-mega-heading">Menu</h2>
          <ul class="qld__header__govuk-mega-list">
            <li><a href="10">Plans</a></li>
            <li><a href="20">DM guideline</a></li>
            <li><a href="30">Awareness and training</a></li>
            <li><a href="40">Resources</a></li>
            <li><a href="50">Partners</a></li>
          </ul>
        </div>
        <div class="col-xs-12 col-md-4">
          <h2 class="qld__header__govuk-mega-heading">Useful links</h2>
          <ul class="qld__header__govuk-mega-list">
            <li><a href="https://www.designsystem.qld.gov.au/">Log in</a></li>
            <li><a href="https://www.designsystem.qld.gov.au/">Contact us</a></li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
"""

content = re.sub(header_pattern, new_header_html, content, flags=re.DOTALL)

# Add our custom CSS and JS
custom_css_js = """
  <style>
    /* GOV.UK Style Header Variables and Base */
    :root {
      --govuk-header-bg: #0b0c0c;
      --govuk-header-text: #ffffff;
      --govuk-header-focus-bg: #fd0;
      --govuk-header-focus-text: #0b0c0c;
      --govuk-header-link: #ffffff;
      --govuk-header-link-hover: #ffffff;
    }
    
    .qld__header--govuk {
      border-bottom: 10px solid #1d70b8;
    }
    
    .qld__header__main--dark {
      background-color: var(--govuk-header-bg);
      color: var(--govuk-header-text);
      padding: 10px 0;
    }
    
    .qld__header__govuk-container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
    }
    
    .qld__header__govuk-brand {
      display: flex;
      align-items: center;
      gap: 15px;
    }
    
    .qld__header__govuk-logo svg {
      fill: var(--govuk-header-text);
      height: 36px;
      width: auto;
    }
    
    .qld__header__govuk-site-name {
      color: var(--govuk-header-link);
      text-decoration: none;
      font-size: 1.5rem;
      font-weight: 700;
      line-height: 1.2;
    }
    
    .qld__header__govuk-site-name:hover {
      text-decoration: underline;
      text-decoration-thickness: 2px;
      text-underline-offset: 3px;
    }
    
    .qld__header__govuk-site-name:focus {
      background-color: var(--govuk-header-focus-bg);
      color: var(--govuk-header-focus-text);
      outline: 3px solid var(--govuk-header-focus-bg);
      box-shadow: 0 -2px var(--govuk-header-focus-bg), 0 4px var(--govuk-header-focus-text);
      text-decoration: none;
    }
    
    /* Search and Menu Actions */
    .qld__header__govuk-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .qld__header__govuk-search {
      display: none; /* hidden on mobile by default */
    }
    
    .qld__header__govuk-search-form {
      display: flex;
    }
    
    .qld__header__govuk-search-input {
      border: 2px solid #0b0c0c;
      padding: 8px 10px;
      font-size: 1.125rem;
      width: 200px;
      height: 40px;
      border-radius: 0;
    }
    
    .qld__header__govuk-search-input:focus {
      outline: 3px solid var(--govuk-header-focus-bg);
      box-shadow: inset 0 0 0 2px #0b0c0c;
    }
    
    .qld__header__govuk-search-button {
      background-color: #f3f2f1;
      border: none;
      width: 40px;
      height: 40px;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
    }
    
    .qld__header__govuk-search-button:hover {
      background-color: #b1b4b6;
    }
    
    .qld__header__govuk-search-button:focus {
      outline: 3px solid var(--govuk-header-focus-bg);
      box-shadow: inset 0 0 0 2px #0b0c0c;
    }
    
    .qld__header__govuk-search-button svg {
      width: 20px;
      height: 20px;
      fill: #0b0c0c;
    }
    
    /* Menu Toggle Button */
    .qld__header__govuk-menu-toggle,
    .qld__header__govuk-search-toggle {
      background: transparent;
      border: none;
      color: var(--govuk-header-text);
      font-size: 1.125rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      padding: 8px;
    }
    
    .qld__header__govuk-menu-toggle:hover,
    .qld__header__govuk-search-toggle:hover {
      text-decoration: underline;
    }
    
    .qld__header__govuk-menu-toggle:focus,
    .qld__header__govuk-search-toggle:focus {
      background-color: var(--govuk-header-focus-bg);
      color: var(--govuk-header-focus-text);
      outline: 3px solid var(--govuk-header-focus-bg);
      text-decoration: none;
    }
    
    .qld__header__govuk-menu-toggle:focus svg,
    .qld__header__govuk-search-toggle:focus svg {
      fill: var(--govuk-header-focus-text);
    }
    
    .qld__header__govuk-menu-toggle svg,
    .qld__header__govuk-search-toggle svg {
      width: 24px;
      height: 24px;
      fill: var(--govuk-header-text);
    }
    
    /* Mega Menu Dropdown */
    .qld__header__govuk-mega-menu {
      background-color: #f3f2f1;
      border-bottom: 1px solid #b1b4b6;
      padding: 20px 0;
    }
    
    .qld__header__govuk-mega-heading {
      font-size: 1.25rem;
      margin-top: 0;
      margin-bottom: 15px;
      border-bottom: 1px solid #b1b4b6;
      padding-bottom: 10px;
    }
    
    .qld__header__govuk-mega-list {
      list-style: none;
      padding: 0;
      margin: 0 0 20px 0;
      columns: 2; /* 2 columns for links */
      column-gap: 2rem;
    }
    
    .qld__header__govuk-mega-list li {
      margin-bottom: 15px;
      break-inside: avoid;
    }
    
    .qld__header__govuk-mega-list a {
      color: #1d70b8;
      text-decoration: underline;
      font-weight: 700;
      font-size: 1.125rem;
    }
    
    .qld__header__govuk-mega-list a:hover {
      color: #003078;
      text-decoration-thickness: max(3px, .1875rem, .12em);
    }
    
    /* Mobile Search Pane */
    .qld__header__govuk-mobile-search-pane {
      background-color: #f3f2f1;
      padding: 15px 0;
      border-top: 1px solid #b1b4b6;
    }
    
    .qld__header__govuk-mobile-search-pane .qld__header__govuk-search-input {
      width: calc(100% - 40px); /* Fill width minus button */
    }
    
    @media (min-width: 992px) {
      .qld__header__govuk-search {
        display: block; /* Show inline search on desktop */
      }
      .qld__header__govuk-search-toggle {
        display: none; /* Hide mobile search toggle on desktop */
      }
      .qld__header__govuk-mega-list {
        columns: 3; /* 3 columns on desktop */
      }
    }
  </style>
  
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // Menu Toggle
      const menuBtn = document.getElementById('govuk-menu-toggle');
      const menuPane = document.getElementById('govuk-mega-menu');
      const menuIcon = menuBtn.querySelector('.qld__header__govuk-menu-icon');
      const menuCloseIcon = menuBtn.querySelector('.qld__header__govuk-close-icon');
      
      // Search Toggle (Mobile)
      const searchBtn = document.getElementById('govuk-search-toggle');
      const searchPane = document.getElementById('govuk-mobile-search');
      const searchIcon = searchBtn.querySelector('.qld__header__govuk-search-icon');
      const searchCloseIcon = searchBtn.querySelector('.qld__header__govuk-search-close-icon');
      
      menuBtn.addEventListener('click', function() {
        const isExpanded = menuBtn.getAttribute('aria-expanded') === 'true';
        menuBtn.setAttribute('aria-expanded', !isExpanded);
        menuPane.style.display = isExpanded ? 'none' : 'block';
        menuIcon.style.display = isExpanded ? 'block' : 'none';
        menuCloseIcon.style.display = isExpanded ? 'none' : 'block';
        
        // Close search if open
        if (searchBtn.getAttribute('aria-expanded') === 'true') {
          searchBtn.click();
        }
      });
      
      searchBtn.addEventListener('click', function() {
        const isExpanded = searchBtn.getAttribute('aria-expanded') === 'true';
        searchBtn.setAttribute('aria-expanded', !isExpanded);
        searchPane.style.display = isExpanded ? 'none' : 'block';
        searchIcon.style.display = isExpanded ? 'block' : 'none';
        searchCloseIcon.style.display = isExpanded ? 'none' : 'block';
        
        // Close menu if open
        if (menuBtn.getAttribute('aria-expanded') === 'true') {
          menuBtn.click();
        }
      });
    });
  </script>
"""

content = content.replace('</head>', custom_css_js + '\n</head>', 1)

with open('/Users/Bec/Dev/qh-design-system/prototypes/logo-lockup-govuk.html', 'w') as f:
    f.write(content)

print("Replacement complete")
