import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔  Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")

def get_fruity_vice_data(fruit):
  fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit}")
  fruit_normalized = pandas.json_normalize(fruityvice_response.json())
  return  fruit_normalized 


try: 
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruity_vice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()
    
    
# streamlit.stop()

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()

# my_cur.execute("SELECT * from pc_rivery_db.public.FRUIT_LOAD_LIST")
# my_data_rows = my_cur.fetchall()
# streamlit.text("The fruit load list contains")
# streamlit.dataframe(my_data_rows)

# new_fruit_choice = streamlit.text_input('What you like to add a fruit?','Add new fruit here')

# streamlit.write('Thank you for adding', new_fruit_choice)\
# my_cur.execute("insert into fruit_load_list_values ('from streamlit')")
# #fruityvice_response = requests.put(f"https://fruityvice.com/api/fruit/{fruit_choice}")
