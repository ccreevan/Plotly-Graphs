import requests
from plotly import offline

# API call information and variables, headers broken?
# modify language variable to create different graphs
language = input('Input a language to query: ')
url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
r = requests.get(url)

# status code 200 desired (success)
print(f"Status code: {r.status_code}")

# stores and prints results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_links.append(f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}</a>")
    stars.append(repo_dict['stargazers_count'])
    labels.append(repo_dict['description'])

data = [{
    'type': 'bar',
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {
            'width': 1.5,
            'color': 'rgb(25, 25, 25)'
        }
    },
    'opacity': .5,
    'x': repo_links,
    'y': stars,
}]
my_layout = {
    'title': f'Top Starred GitHub {language.title()} Projects',
    'xaxis': {
        'title': 'Repo',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    }
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=f"{language}_repos.html")
