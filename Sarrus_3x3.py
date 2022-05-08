{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Sarrus 3x3.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMDnynzsccpTPm5qPQwM3fb",
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
        "<a href=\"https://colab.research.google.com/github/gamossini/Matematica_II/blob/main/Sarrus_3x3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np"
      ],
      "metadata": {
        "id": "T5mzZBW1TgV9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# produto vetorial\n",
        "# |a11 a12 a13|\n",
        "# |a21 a22 a23|\n",
        "# |a31 a32 a33|\n",
        "\n",
        "#Regra de Sarrus\n",
        "# |a11 a12 a13| a11 a12|\n",
        "# |a21 a22 a23| a21 a22|\n",
        "# |a31 a32 a33| a31 a32|\n",
        "\n",
        "a11 = 2\n",
        "a12 = 1\n",
        "a13 = -1\n",
        "a21 = 1\n",
        "a22 = 3\n",
        "a23 = -1\n",
        "a31 = 5\n",
        "a32 = -2\n",
        "a33 = 10\n",
        "\n",
        "def det2x2(m):\n",
        "  return m[0][0] * m[1][1] - m[0][1] * m[1][0]\n",
        "\n",
        "matrix = [\n",
        "          [a11, a12, a13],\n",
        "          [a21, a22, a23],\n",
        "          [a31, a32, a33]\n",
        "]\n",
        "\n",
        "print(\"Matix: \")\n",
        "for array in matrix: print(array)\n",
        "\n",
        "print()\n",
        "\n",
        "a,b,c = matrix[0]\n",
        "\n",
        "efhi = [x[1:] for x in matrix[1:]]\n",
        "\n",
        "dfgi = [x[::2]for x in matrix [1:]]\n",
        "\n",
        "degh = [x[0:2]for x in matrix[1:]]\n",
        "\n",
        "det = (\n",
        "    a* det2x2(efhi)\n",
        "    - b * det2x2(dfgi)\n",
        "    + c * det2x2(degh)\n",
        ")\n",
        "\n",
        "print(f\"Determinante da matrix seguindo a Regra de Sarrus é: {det}\")\n"
      ],
      "metadata": {
        "id": "NySWU3Y4Ty0L",
        "outputId": "a1d75822-b24e-4f0c-dcd4-ce0aa8b39bd2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Matix: \n",
            "[2, 1, -1]\n",
            "[1, 3, -1]\n",
            "[5, -2, 10]\n",
            "\n",
            "Determinante da matrix seguindo a Regra de Sarrus é: 58\n"
          ]
        }
      ]
    }
  ]
}