{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO5DxpWzpxnvDiCcoTShUT4",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/frivblon1712/Unidad4IA/blob/main/Practica1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "TufjpxQHfnza"
      },
      "outputs": [],
      "source": [
        "import tensorflow as tf\n",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "celcius = np.array([-15, -5, 0, 5, 15], dtype=float)\n",
        "fahrenheit = np.array([5, 23, 32, 41, 59], dtype=float)"
      ],
      "metadata": {
        "id": "QC5wCHClftFJ"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "capa = tf.keras.layers.Dense(units=1, input_shape=[1])\n",
        "modelo = tf.keras.Sequential([capa])"
      ],
      "metadata": {
        "id": "gqV8ASeufuZq"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "modelo.compile(\n",
        "    optimizer = tf.keras.optimizers.Adam(0.1),\n",
        "    loss='mean_squared_error'\n",
        ")"
      ],
      "metadata": {
        "id": "0pKj_NHbfvmS"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"comenzando entrenamiento\")\n",
        "historial=modelo.fit(celcius, fahrenheit, epochs=1000, verbose=False)\n",
        "print(\"modelo entrenado!!!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dRF6t9ypfw0b",
        "outputId": "934c279b-1a64-44a8-8490-ccb016490edc"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "comenzando entrenamiento\n",
            "modelo entrenado!!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "plt.xlabel(\"# Epoca\")\n",
        "plt.ylabel(\"Magnitud de perdida\")\n",
        "plt.plot(historial.history[\"loss\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 466
        },
        "id": "PL8apRTSfyWU",
        "outputId": "6161ad8f-44aa-4188-d691-1cdc948fed28"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7ff078933970>]"
            ]
          },
          "metadata": {},
          "execution_count": 6
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkQAAAGwCAYAAABIC3rIAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABQ/0lEQVR4nO3deXhTVf4/8PdN06R7utGmhXRhsWwtlK0WAWVASkFA9OvCIruMggvgKDIKIqhFcBhQUWRGRAWF4SeCIIJlLUvZKYUCZSu0QFuW0qYLXZLc3x+lgdgCDSS5afN+Pc99TM49ST65DOQ95557riCKoggiIiIiByaTugAiIiIiqTEQERERkcNjICIiIiKHx0BEREREDo+BiIiIiBweAxERERE5PAYiIiIicnhyqQuoCwwGAy5fvgxPT08IgiB1OURERFQLoiiisLAQwcHBkMnuPQbEQFQLly9fhkajkboMIiIiegBZWVlo1KjRPfswENWCp6cngMoD6uXlJXE1REREVBtarRYajcb4O34vDES1UHWazMvLi4GIiIiojqnNdBdOqiYiIiKHx0BEREREDo+BiIiIiBweAxERERE5PAYiIiIicngMREREROTwGIiIiIjI4TEQERERkcNjICIiIiKHx0BEREREDo+BiIiIiBweAxERERE5PAYiCekNInIKSnHherHUpRARETk0BiIJ5WhL8WjCZjw5N0nqUoiIiBwaA5GE3JydAADlegN0eoPE1RARETkuBiIJuSqcjI9vVuglrISIiMixMRBJSCmXQRAqH98sZyAiIiKSCgORhARBMJ424wgRERGRdBiIJOaqkAMASjhCREREJBkGIom5Kir/CBiIiIiIpMNAJDE358oRolKeMiMiIpIMA5HEqq404wgRERGRdBiIJObqXBWIdBJXQkRE5LgYiCTmdmuEiKfMiIiIpMNAJDGeMiMiIpIeA5HEXLkOERERkeQYiCRWdcqMK1UTERFJh4FIYi48ZUZERCQ5BiKJVa1DxFNmRERE0mEgkhhPmREREUmPgUhit0+ZcR0iIiIiqTAQSez23e4NEldCRETkuBiIJHb7lBlHiIiIiKQiaSBKSkpCv379EBwcDEEQsHr1apP9giDUuM2ZM8fYJywsrNr+WbNmmbxPamoqunbtChcXF2g0GsyePdsWX69WeJUZERGR9CQNRMXFxWjT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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"realizar una prediccion!!!\")\n",
        "resultado = modelo.predict([100.0])\n",
        "print (\"el resultado es\" + str(resultado) + \"galones!!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UX8ZKVJSf0Ds",
        "outputId": "0e6bd623-69cc-4796-c16a-690ef3d62635"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "realizar una prediccion!!!\n",
            "1/1 [==============================] - 0s 96ms/step\n",
            "el resultado es[[211.9783]]galones!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "modelo.save('celsuis_a_fahrenheit.h5')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gg08CA6Tf2k2",
        "outputId": "566ef848-1fbe-49f8-e24c-61cb1f2e13c4"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3079: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.\n",
            "  saving_api.save_model(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mk89a5sef2-1",
        "outputId": "79a08eca-bccb-4b9b-ab55-3c825e55eab5"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "celsuis_a_fahrenheit.h5  sample_data\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install tensorflowjs"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "JufQcVsvf4y-",
        "outputId": "83b68cb0-2879-48ed-fc9d-eabfae5027a1"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting tensorflowjs\n",
            "  Downloading tensorflowjs-4.13.0-py3-none-any.whl (89 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m89.2/89.2 kB\u001b[0m \u001b[31m2.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: flax>=0.7.2 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (0.7.5)\n",
            "Requirement already satisfied: importlib_resources>=5.9.0 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (6.1.1)\n",
            "Requirement already satisfied: jax>=0.4.13 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (0.4.20)\n",
            "Requirement already satisfied: jaxlib>=0.4.13 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (0.4.20+cuda11.cudnn86)\n",
            "Requirement already satisfied: tensorflow<3,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (2.14.0)\n",
            "Collecting tensorflow-decision-forests>=1.5.0 (from tensorflowjs)\n",
            "  Downloading tensorflow_decision_forests-1.8.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (15.3 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m15.3/15.3 MB\u001b[0m \u001b[31m69.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: six<2,>=1.16.0 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (1.16.0)\n",
            "Requirement already satisfied: tensorflow-hub>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (0.15.0)\n",
            "Requirement already satisfied: packaging~=23.1 in /usr/local/lib/python3.10/dist-packages (from tensorflowjs) (23.2)\n",
            "Requirement already satisfied: numpy>=1.22 in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (1.23.5)\n",
            "Requirement already satisfied: msgpack in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (1.0.7)\n",
            "Requirement already satisfied: optax in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (0.1.7)\n",
            "Requirement already satisfied: orbax-checkpoint in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (0.4.2)\n",
            "Requirement already satisfied: tensorstore in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (0.1.45)\n",
            "Requirement already satisfied: rich>=11.1 in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (13.7.0)\n",
            "Requirement already satisfied: typing-extensions>=4.2 in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (4.5.0)\n",
            "Requirement already satisfied: PyYAML>=5.4.1 in /usr/local/lib/python3.10/dist-packages (from flax>=0.7.2->tensorflowjs) (6.0.1)\n",
            "Requirement already satisfied: ml-dtypes>=0.2.0 in /usr/local/lib/python3.10/dist-packages (from jax>=0.4.13->tensorflowjs) (0.2.0)\n",
            "Requirement already satisfied: opt-einsum in /usr/local/lib/python3.10/dist-packages (from jax>=0.4.13->tensorflowjs) (3.3.0)\n",
            "Requirement already satisfied: scipy>=1.9 in /usr/local/lib/python3.10/dist-packages (from jax>=0.4.13->tensorflowjs) (1.11.3)\n",
            "Requirement already satisfied: absl-py>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (1.4.0)\n",
            "Requirement already satisfied: astunparse>=1.6.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (1.6.3)\n",
            "Requirement already satisfied: flatbuffers>=23.5.26 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (23.5.26)\n",
            "Requirement already satisfied: gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (0.5.4)\n",
            "Requirement already satisfied: google-pasta>=0.1.1 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (0.2.0)\n",
            "Requirement already satisfied: h5py>=2.9.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (3.9.0)\n",
            "Requirement already satisfied: libclang>=13.0.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (16.0.6)\n",
            "Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (3.20.3)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (67.7.2)\n",
            "Requirement already satisfied: termcolor>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (2.3.0)\n",
            "Requirement already satisfied: wrapt<1.15,>=1.11.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (1.14.1)\n",
            "Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.23.1 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (0.34.0)\n",
            "Requirement already satisfied: grpcio<2.0,>=1.24.3 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (1.59.2)\n",
            "Requirement already satisfied: tensorboard<2.15,>=2.14 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (2.14.1)\n",
            "Requirement already satisfied: tensorflow-estimator<2.15,>=2.14.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (2.14.0)\n",
            "Requirement already satisfied: keras<2.15,>=2.14.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow<3,>=2.13.0->tensorflowjs) (2.14.0)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (from tensorflow-decision-forests>=1.5.0->tensorflowjs) (1.5.3)\n",
            "Collecting tensorflow<3,>=2.13.0 (from tensorflowjs)\n",
            "  Downloading tensorflow-2.15.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (475.2 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m475.2/475.2 MB\u001b[0m \u001b[31m1.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: wheel in /usr/local/lib/python3.10/dist-packages (from tensorflow-decision-forests>=1.5.0->tensorflowjs) (0.41.3)\n",
            "Collecting wurlitzer (from tensorflow-decision-forests>=1.5.0->tensorflowjs)\n",
            "  Downloading wurlitzer-3.0.3-py3-none-any.whl (7.3 kB)\n",
            "Collecting tensorboard<2.16,>=2.15 (from tensorflow<3,>=2.13.0->tensorflowjs)\n",
            "  Downloading tensorboard-2.15.1-py3-none-any.whl (5.5 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m5.5/5.5 MB\u001b[0m \u001b[31m98.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting tensorflow-estimator<2.16,>=2.15.0 (from tensorflow<3,>=2.13.0->tensorflowjs)\n",
            "  Downloading tensorflow_estimator-2.15.0-py2.py3-none-any.whl (441 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m442.0/442.0 kB\u001b[0m \u001b[31m42.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting keras<2.16,>=2.15.0 (from tensorflow<3,>=2.13.0->tensorflowjs)\n",
            "  Downloading keras-2.15.0-py3-none-any.whl (1.7 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.7/1.7 MB\u001b[0m \u001b[31m79.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=11.1->flax>=0.7.2->tensorflowjs) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=11.1->flax>=0.7.2->tensorflowjs) (2.16.1)\n",
            "Requirement already satisfied: google-auth<3,>=1.6.3 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2.17.3)\n",
            "Requirement already satisfied: google-auth-oauthlib<2,>=0.5 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (1.0.0)\n",
            "Requirement already satisfied: markdown>=2.6.8 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.5.1)\n",
            "Requirement already satisfied: requests<3,>=2.21.0 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2.31.0)\n",
            "Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (0.7.2)\n",
            "Requirement already satisfied: werkzeug>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.0.1)\n",
            "Requirement already satisfied: chex>=0.1.5 in /usr/local/lib/python3.10/dist-packages (from optax->flax>=0.7.2->tensorflowjs) (0.1.7)\n",
            "Requirement already satisfied: etils[epath,epy] in /usr/local/lib/python3.10/dist-packages (from orbax-checkpoint->flax>=0.7.2->tensorflowjs) (1.5.2)\n",
            "Requirement already satisfied: nest_asyncio in /usr/local/lib/python3.10/dist-packages (from orbax-checkpoint->flax>=0.7.2->tensorflowjs) (1.5.8)\n",
            "Requirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.10/dist-packages (from pandas->tensorflow-decision-forests>=1.5.0->tensorflowjs) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas->tensorflow-decision-forests>=1.5.0->tensorflowjs) (2023.3.post1)\n",
            "Requirement already satisfied: dm-tree>=0.1.5 in /usr/local/lib/python3.10/dist-packages (from chex>=0.1.5->optax->flax>=0.7.2->tensorflowjs) (0.1.8)\n",
            "Requirement already satisfied: toolz>=0.9.0 in /usr/local/lib/python3.10/dist-packages (from chex>=0.1.5->optax->flax>=0.7.2->tensorflowjs) (0.12.0)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (5.3.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (0.3.0)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.10/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (4.9)\n",
            "Requirement already satisfied: requests-oauthlib>=0.7.0 in /usr/local/lib/python3.10/dist-packages (from google-auth-oauthlib<2,>=0.5->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (1.3.1)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich>=11.1->flax>=0.7.2->tensorflowjs) (0.1.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2023.7.22)\n",
            "Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib/python3.10/dist-packages (from werkzeug>=1.0.1->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (2.1.3)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from etils[epath,epy]->orbax-checkpoint->flax>=0.7.2->tensorflowjs) (2023.6.0)\n",
            "Requirement already satisfied: zipp in /usr/local/lib/python3.10/dist-packages (from etils[epath,epy]->orbax-checkpoint->flax>=0.7.2->tensorflowjs) (3.17.0)\n",
            "Requirement already satisfied: pyasn1<0.6.0,>=0.4.6 in /usr/local/lib/python3.10/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (0.5.0)\n",
            "Requirement already satisfied: oauthlib>=3.0.0 in /usr/local/lib/python3.10/dist-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<2,>=0.5->tensorboard<2.16,>=2.15->tensorflow<3,>=2.13.0->tensorflowjs) (3.2.2)\n",
            "Installing collected packages: wurlitzer, tensorflow-estimator, keras, tensorboard, tensorflow, tensorflow-decision-forests, tensorflowjs\n",
            "  Attempting uninstall: tensorflow-estimator\n",
            "    Found existing installation: tensorflow-estimator 2.14.0\n",
            "    Uninstalling tensorflow-estimator-2.14.0:\n",
            "      Successfully uninstalled tensorflow-estimator-2.14.0\n",
            "  Attempting uninstall: keras\n",
            "    Found existing installation: keras 2.14.0\n",
            "    Uninstalling keras-2.14.0:\n",
            "      Successfully uninstalled keras-2.14.0\n",
            "  Attempting uninstall: tensorboard\n",
            "    Found existing installation: tensorboard 2.14.1\n",
            "    Uninstalling tensorboard-2.14.1:\n",
            "      Successfully uninstalled tensorboard-2.14.1\n",
            "  Attempting uninstall: tensorflow\n",
            "    Found existing installation: tensorflow 2.14.0\n",
            "    Uninstalling tensorflow-2.14.0:\n",
            "      Successfully uninstalled tensorflow-2.14.0\n",
            "Successfully installed keras-2.15.0 tensorboard-2.15.1 tensorflow-2.15.0 tensorflow-decision-forests-1.8.1 tensorflow-estimator-2.15.0 tensorflowjs-4.13.0 wurlitzer-3.0.3\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "keras",
                  "tensorboard",
                  "tensorflow"
                ]
              }
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!mkdir temperatura"
      ],
      "metadata": {
        "id": "ol8S2CAHf6UW"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!tensorflowjs_converter --input_format keras celsuis_a_fahrenheit.h5 temperatura"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6yYoX1n4f9E_",
        "outputId": "577b3558-d196-41f1-fd1a-e00b81421d74"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2023-11-30 04:35:23.330427: I external/local_tsl/tsl/cuda/cudart_stub.cc:31] Could not find cuda drivers on your machine, GPU will not be used.\n",
            "2023-11-30 04:35:23.570754: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:9261] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered\n",
            "2023-11-30 04:35:23.570831: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:607] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered\n",
            "2023-11-30 04:35:23.579630: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1515] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered\n",
            "2023-11-30 04:35:23.632495: I external/local_tsl/tsl/cuda/cudart_stub.cc:31] Could not find cuda drivers on your machine, GPU will not be used.\n",
            "2023-11-30 04:35:23.632857: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\n",
            "To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\n",
            "2023-11-30 04:35:28.785185: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls temperatura"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dGzA58Hrf-YA",
        "outputId": "d4214c31-02db-4a36-8efc-40b124678b00"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "group1-shard1of1.bin  model.json\n"
          ]
        }
      ]
    }
  ]
}