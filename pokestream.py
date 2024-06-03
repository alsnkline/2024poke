import streamlit as st
import requests as rq
import json
import pandas as pd

url = "https://pokeapi.co/api/v2/pokemon/"
all_results = []
counter = 0

while url:

    response = rq.get(url)
    data = response.json()
    #print(json.dumps(response.json(), indent=4))
    
    all_results.extend(data['results'])
    url = data['next']
    
    counter += 1
    # Print a '.' every 5 loops
    if counter % 5 == 0:
        print('.', end='', flush=True)

df = pd.DataFrame(all_results)
#print(df)

#st.write("Here's a table of all pokemon:")
#df

st.title('Pokémon Selector')
# Add a placeholder for the selectbox
options = ['Select a Pokémon'] + df['name'].tolist()

chosen_pokemon = st.sidebar.selectbox(
    'Which pokemon do you like best?',
    options,
    index=0
)

if chosen_pokemon != 'Select a Pokémon':
    st.write('You selected: ', chosen_pokemon)
    pokemon_url = "https://pokeapi.co/api/v2/pokemon/"+chosen_pokemon
    response2 = rq.get(pokemon_url)
    data2 = response2.json()
    print(json.dumps(data2, indent=4))

    st.metric(label='Base Experience', value=data2['base_experience'])

    col1, col2 = st.columns(2)
    col1.metric(label='Height', value=data2['height'])
    col2.metric(label='Weight', value=data2['weight'])

    col3, col4 = st.columns(2)
    col3.metric(label='Order', value=data2['order'])
    col4.metric(label='ID', value=data2['id'])

    # Extract and display images
    sprites = data2['sprites']
    image_urls = [sprites['front_default'], sprites['back_default'],
                  sprites['front_shiny'], sprites['back_shiny']]

    # Create columns for the images
    cols = st.columns(len(image_urls))

    for col, url in zip(cols, image_urls):
        if url:
            col.image(url)

    # Display full Pokémon details using Strealit json displayer
    st.json(data2)

else:
    st.write('Please select a Pokémon.')