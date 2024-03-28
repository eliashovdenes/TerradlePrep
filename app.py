import streamlit as st

st.set_page_config(page_title="Terradle practice!", page_icon=":deciduous_tree:", layout="wide")


weapon_name = "Zenith"

all_correct = False

correct_answers = {
    'damage_type': 'Melee',  # TODO: Replace with the correct value
    'damage': 190,           # TODO: Replace with the correct value
    'knockback': 'Average',  # TODO: Replace with the correct value
    'speed': 'Fast',         # TODO: Replace with the correct value
    'rarity': 'Pink',        # TODO: Replace with the correct value
    'autoswing': 'Yes',      # TODO: Replace with the correct value
    'material': 'Yes',       # TODO: Replace with the correct value
    'obtained': 'Drop'       # TODO: Replace with the correct value
}

with st.container():
    left, center, right = st.columns(3)
    with center:
            st.title("Terradle Practice", anchor=False)
            st.write("Guess the weapons attributes!")

            #name of the weapon
            nameOfWeapon = "Weapon Name: " + weapon_name
            # st.subheader(nameOfWeapon, anchor=False)

with st.container():
        one, two, three, four, five, six, seven, eight, nine = st.columns(9)
        with one:
            st.subheader("Current Weapon:", anchor=False)
             #picture
            url = "zenith.png"
            st.image(url, width=50, caption="Zenith" )

            hide_img_fs = '''
            <style>
            button[title="View fullscreen"]{
                visibility: hidden;}
            </style>
            '''

            st.markdown(hide_img_fs, unsafe_allow_html=True)


        with two:
            # Damage Type Dropdown
            damage_type_options = ['----', 'Melee', 'Ranged', 'Summoner', 'Magic']
    
            # If the correct answer has been given, disable the dropdown, otherwise enable it.
            damage_type_disabled = st.session_state.get('damage_type_correct', False)
            selected_damage_type = st.selectbox(
                "Select the damage type:",
                damage_type_options,
                index=0,
                disabled=damage_type_disabled
            )

            # Button to check the damage type, only enabled if the correct answer hasn't been given yet
            if not damage_type_disabled:
                if st.button('Check Damage Type'):
                    if selected_damage_type == correct_answers['damage_type']:
                        
                        # Update the session state to reflect the correct answer has been given
                        st.session_state['damage_type_correct'] = True
                        # Disable the dropdown immediately
                        damage_type_disabled = True
                        st.rerun()
                        
                    else:
                        st.error("Incorrect. Try again.")

            else:
                st.success("Correct!")


        
        with three:

            
            
            # Button to check the damage input
            damage_amount_disabled = st.session_state.get('damage_amount_correct', False)


            # Input for damage
            damage_input = st.text_input("Enter the damage amount:", disabled=damage_amount_disabled)
            damage_input = int(damage_input) if damage_input else None

            if not damage_amount_disabled:
                if st.button('Check Damage Amount') or damage_input:
                    if damage_input == correct_answers['damage']:
                        st.session_state['damage_amount_correct'] = True
                        damage_amount_disabled = True
                        st.rerun()
                    else:
                        if damage_input:
                            if damage_input > correct_answers['damage']:
                                st.error("Too high!")
                            if damage_input < correct_answers['damage']:
                                st.error("Too low!")
            
            else:
                st.success("Correct!")
            

           

        


with st.container():
     if all_correct == True:
        st.write("You got all the answers correct!")

        st.button("Next Weapon")


# with st.container():
#         # Button to check the damage input
#             if st.button("Check Damage") and damage_input and damageType_input:
#                 if damage_input.strip() == "190":  # Strip is used to remove any leading/trailing whitespace
#                     st.text("Correct!")
#                 else:
#                     st.text("Incorrect. Try again.")

#             else:
#                 st.text("Please enter a value.")



            