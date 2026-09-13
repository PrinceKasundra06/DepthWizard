import sys

with open("website/frontend/css/style.css", "r") as f:
    css = f.read()

# Let's just find the /* Sidebar Menu Items */ and inject everything that was lost right before it.
missing_css = """
.draftly-header-left {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.draftly-logo {
    font-weight: 600;
    font-size: 14px;
    letter-spacing: -0.02em;
    color: #fff !important;
    text-decoration: none !important;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.draftly-logo i {
    color: rgba(255, 255, 255, 0.5);
}

.draftly-header-right {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.draftly-btn-small {
    display: inline-flex;
    align-items: center;
    gap: 0.375rem;
    height: 32px;
    padding: 0 0.75rem;
    border-radius: 8px;
    font-size: 11px;
    font-weight: 600;
    background: rgba(255, 255, 255, 0.04);
    color: rgba(255, 255, 255, 0.7) !important;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.2s;
    text-decoration: none !important;
    cursor: pointer;
}

.draftly-btn-small:hover {
    background: rgba(255, 255, 255, 0.08);
    color: #ffffff !important;
    border-color: rgba(255, 255, 255, 0.18);
}

.draftly-btn-primary {
    background: #ffffff;
    color: #000000 !important;
    border: 1px solid #ffffff;
}

.draftly-btn-primary:hover {
    background: rgba(255, 255, 255, 0.9);
}

.draftly-sidebar-header {
    padding: 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.draftly-sidebar-title {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: rgba(255, 255, 255, 0.6);
}

.draftly-sidebar-content {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.draftly-sidebar-footer {
    padding: 1rem;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    background-color: rgba(0, 0, 0, 0.2);
}
"""

css = css.replace("/* Sidebar Menu Items */", missing_css + "\n/* Sidebar Menu Items */")

with open("website/frontend/css/style.css", "w") as f:
    f.write(css)

print("Restored missing CSS classes!")
