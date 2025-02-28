{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a96dd39c-66d7-448c-9fbb-bfd4d6fac759",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load the trained model\n",
    "with open('placement_model.pkl', 'rb') as model_file:\n",
    "    model = pickle.load(model_file)\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"📊 Placement Package Predictor\")\n",
    "st.write(\"Enter your CGPA to predict your expected package.\")\n",
    "\n",
    "# User input for CGPA\n",
    "cgpa = st.number_input(\"Enter your CGPA:\", min_value=0.0, max_value=10.0, step=0.01)\n",
    "\n",
    "# Predict button\n",
    "if st.button(\"Predict Package\"):\n",
    "    if cgpa > 0:\n",
    "        # Convert input into array for model prediction\n",
    "        input_data = np.array([[cgpa]])\n",
    "        predicted_package = model.predict(input_data)\n",
    "        \n",
    "        # Display prediction\n",
    "        st.success(f\"🎓 Expected Package: ₹{predicted_package[0]:.2f} LPA\")\n",
    "    else:\n",
    "        st.warning(\"⚠️ Please enter a valid CGPA.\")\n",
    "\n",
    "# Footer\n",
    "st.markdown(\"---\")\n",
    "st.markdown(\"🔍 *Developed with Streamlit and Machine Learning*\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
