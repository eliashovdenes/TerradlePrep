import streamlit as st

st.set_page_config(page_title="Terradle practice!", page_icon=":deciduous_tree:", layout="wide")


weapon_name = "Zenith"

with st.container():
        left, center, right = st.columns(3)
        with center:

            #title
            st.title("Terradle Practice", anchor=False)
            st.write("Guess the weapons attributes!")

            #name of the weapon
            nameOfWeapon = "Weapon Name: " + weapon_name
            st.subheader(nameOfWeapon, anchor=False)
            #picture
            url = "image.png"
            st.image(url, width=100)

            hide_img_fs = '''
            <style>
            button[title="View fullscreen"]{
                visibility: hidden;}
            </style>
            '''

            st.markdown(hide_img_fs, unsafe_allow_html=True)

            
            # Input for damage
            damage_input = st.text_input("Enter the damage amount:")

            # Button to check the damage input
            if st.button("Check Damage") or damage_input:
                if damage_input.strip() == "190":  # Strip is used to remove any leading/trailing whitespace
                    st.text("Correct!")
                else:
                    st.text("Incorrect. Try again.")


            