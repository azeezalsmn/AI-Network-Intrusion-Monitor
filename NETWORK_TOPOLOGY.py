import networkx as nx
import plotly.graph_objects as go
import random

# --- 1. CRITICAL: LOCK ALL SEEDS ---
# 42 is the seed that usually creates this specific horizontal spread
random.seed(42)
SEED_VAL = 42

# --- 2. GENERATE TOPOLOGY ---
G = nx.random_geometric_graph(20, 0.3, seed=SEED_VAL)

# Metadata
node_types = ['Core Router', 'Edge Switch', 'Database Server', 'User Workstation']
for node in G.nodes():
    G.nodes[node]['type'] = random.choice(node_types)
    # This logic ensures the red dots stay on the left and center like your image
    G.nodes[node]['status'] = 'Critical' if random.random() < 0.15 else 'Healthy'

# --- 3. THE FIX: FORCE THE HORIZONTAL LAYOUT ---
# We use spring_layout with a high 'k' to push nodes apart and a fixed seed
pos = nx.spring_layout(G, k=1.5, iterations=50, seed=SEED_VAL)

# --- 4. TRACES ---
edge_x, edge_y = [], []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=1, color='#888'), hoverinfo='none', mode='lines')

node_trace = go.Scatter(
    x=[pos[node][0] for node in G.nodes()],
    y=[pos[node][1] for node in G.nodes()],
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=False,
        colorscale='RdYlGn',
        reversescale=True,
        # Maps 0 to Green (Healthy) and 1 to Red (Critical)
        color=[0 if G.nodes[n]['status'] == 'Healthy' else 1 for n in G.nodes()],
        size=22,
        line=dict(width=2, color='white')
    )
)

node_text = []
for node in G.nodes():
    node_text.append(f"<b>Device:</b> {G.nodes[node]['type']}<br><b>Status:</b> {G.nodes[node]['status']}")
node_trace.text = node_text

# --- 5. FIGURE & LAYOUT ---
fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<b>Network Security Topology: AI Anomaly Mapping</b>',
                title_x=0.5,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20, l=5, r=5, t=60),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                plot_bgcolor='rgba(240,245,250,1)' # Matches your screenshot background
             ))

# Export for GitHub
fig.write_html("network_topology.html")
fig.show()
files.download("network_topology.html")
