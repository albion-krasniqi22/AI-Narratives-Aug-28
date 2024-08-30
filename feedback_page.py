import streamlit as st
import pandas as pd
import os

def feedback_page():
    st.title('Feedback Records')
    feedback_file = 'feedback.csv'
    feedback_password = "feedback"

    # Initialize session state variables if they do not exist
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'show_confirm' not in st.session_state:
        st.session_state.show_confirm = False

    # Authentication logic
    if not st.session_state.authenticated:
        # Show login form if not authenticated
        with st.form(key='login_form'):
            password = st.text_input("Enter password to view feedback records", type="password")
            login_button = st.form_submit_button("Login")
            
            if login_button:
                if password == feedback_password:
                    st.session_state.authenticated = True
                    st.session_state.show_confirm = False  # Reset the confirm flag
                    st.success("Logged in successfully.")
                    # Set query params to ensure page updates
                    st.experimental_set_query_params(logged_in=True)
                else:
                    st.error("Incorrect password.")
    else:
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.show_confirm = False
            # Update the query parameters to force an update
            st.experimental_set_query_params(logged_in=False)

        if os.path.exists(feedback_file):
            feedback_df = pd.read_csv(feedback_file)
            st.dataframe(feedback_df)

            if st.button("Delete all feedback records"):
                st.session_state.show_confirm = True

            # Confirmation dialog for deletion
            if st.session_state.show_confirm:
                st.warning("Are you sure you want to delete all feedback records?")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Yes, delete"):
                        delete_records(feedback_file)
                with col2:
                    if st.button("Cancel"):
                        st.session_state.show_confirm = False
        else:
            st.info("No feedback records found.")

def delete_records(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        st.success("All feedback records have been deleted.")
    st.session_state.show_confirm = False

if __name__ == "__main__":
    feedback_page()