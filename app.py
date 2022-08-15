{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "c1b649e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "447e2e4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "026f1929",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        rates = float(request.form.get(\"rates\"))\n",
    "        print(rates)\n",
    "        model1 = joblib.load(\"regression_DBS\")\n",
    "        r1 = model1.predict([[rates]])\n",
    "        model2 = joblib.load(\"tree_DBS\")\n",
    "        r2 = model2.predict([[rates]])\n",
    "        return(render_template(\"index.html\",result1=r1,result2=r2))\n",
    "    else:\n",
    "        return(render_template(\"index.html\",result1=\"waiting\",result2=\"waiting\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "294a76fb",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:1111/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [13/Aug/2022 12:18:24] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/lauren/opt/anaconda3/lib/python3.9/site-packages/sklearn/base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "/Users/lauren/opt/anaconda3/lib/python3.9/site-packages/sklearn/base.py:450: UserWarning: X does not have valid feature names, but DecisionTreeRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [13/Aug/2022 12:18:28] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [13/Aug/2022 14:43:18] \"GET / HTTP/1.1\" 200 -\n",
      "/Users/lauren/opt/anaconda3/lib/python3.9/site-packages/sklearn/base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "/Users/lauren/opt/anaconda3/lib/python3.9/site-packages/sklearn/base.py:450: UserWarning: X does not have valid feature names, but DecisionTreeRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [13/Aug/2022 14:43:22] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.5\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/lauren/opt/anaconda3/lib/python3.9/site-packages/sklearn/base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "/Users/lauren/opt/anaconda3/lib/python3.9/site-packages/sklearn/base.py:450: UserWarning: X does not have valid feature names, but DecisionTreeRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [13/Aug/2022 14:43:25] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [15/Aug/2022 13:40:59] \"GET / HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\": \n",
    "    app.run(host=\"127.0.0.1\",port=int(\"1111\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a328fc4",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
