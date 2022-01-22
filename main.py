news_article = [{
    'id':'888',
    'Title': 'Bheemla Nayak Movie Release',
    'Description':'The movie release is postponed',
    'Date':'08-01-2022',
    'Type':'Entertainment'
},
    {
    'id': '999',
    'Title': 'Pro kabbadi',
    'Description': 'Today we are having telugu taitans match',
    'Date': '08-01-2022',
    'Type': 'Sports'
},
    {
    'id':'777',
    'Title': 'Pushpa OTT Release',
    'Description':'The movie is released in prime video',
    'Date':'07-01-2022',
    'Type':'Entertainment'
    },
    {
    'id': '111',
    'Title': 'Omicron',
    'Description': 'There is a fast spread of new variant omicron in the world',
    'Date': '04-01-2022',
    'Type': 'General'
     }]
for d in news_article:
    if d['Type'] == 'Entertainment':
     print(d)