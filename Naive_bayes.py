{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Female']\n"
     ]
    }
   ],
   "source": [
    "from sklearn.naive_bayes import GaussianNB\n",
    "\n",
    "gnb = GaussianNB()\n",
    "\n",
    "\"\"\"[height,weight]\"\"\"\n",
    "x = [[190,44],[180,50],[120,67],[111,54],[98,64],[110,54]]\n",
    "y = [\"Female\",\"Female\",\"Male\",\"Male\",\"Female\",\"Female\"]\n",
    "\n",
    "gnb = gnb.fit(x,y)\n",
    "\n",
    "predicti = gnb.predict([[20,66]])\n",
    "\n",
    "print(predicti)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
