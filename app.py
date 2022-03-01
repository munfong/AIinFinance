#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask


# In[4]:


app = Flask(__name__)


# In[5]:


from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        Nikkei = request.form.get("Nikkei")
        print(Nikkei)
        model1 = joblib.load("STI_Regression")
        pred1 = model1.predict([[Nikkei]])
        str1 = "The prediction for STI using Regression is : " + str(pred1)
        return(render_template("index.html", result1 = str1))
    else:
        return(render_template("index.html", result1 = "2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




