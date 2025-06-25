import graphviz

# Create a new directed graph
dot = graphviz.Digraph(comment='Full Web Application Architecture')

# Add nodes for each component
dot.node('U', 'User')
dot.node('R', 'Recursive DNS Resolver (ISP/Public)')
dot.node('G', 'GeoDNS (Authoritative DNS)')
dot.node('C', 'CDN (e.g., Cloudflare)')
dot.node('L', 'Load Balancer')
dot.node('A1', 'Application Server 1')
dot.node('A2', 'Application Server 2')
dot.node('DB', 'Database')

# Add edges to show the flow of a user request
dot.edge('U', 'R', 'DNS Request')
dot.edge('R', 'G', 'Query Authoritative DNS')
dot.edge('G', 'R', 'Return Geo-based IP')
dot.edge('R', 'U', 'Return IP to User')
dot.edge('U', 'C', 'Request to CDN')
dot.edge('C', 'L', 'Forward to Load Balancer')
dot.edge('L', 'A1', 'Route to App Server 1')
dot.edge('L', 'A2', 'Route to App Server 2')
dot.edge('A1', 'DB', 'Query Database')
dot.edge('A2', 'DB', 'Query Database')
dot.edge('DB', 'A1', 'Return Data')
dot.edge('DB', 'A2', 'Return Data')
dot.edge('A1', 'L', 'Return to Load Balancer')
dot.edge('A2', 'L', 'Return to Load Balancer')
dot.edge('L', 'C', 'Return to CDN')
dot.edge('C', 'U', 'Return to User')

# Save the diagram as a PDF file
dot.render('web_application_architecture', format='pdf')

# Print a success message
print("The diagram of the full web application architecture has been successfully created and saved as 'web_application_architecture.pdf'.")

