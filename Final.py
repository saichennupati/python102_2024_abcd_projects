{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO06Y/KWEB3uZMMeyPYKFJI",
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
        "<a href=\"https://colab.research.google.com/github/sjasthi/python102_2024_abcd_projects/blob/main/Final.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 226
        },
        "id": "nM0i4bUyVsWm",
        "outputId": "2c18dab7-159b-422c-f612-283b20f2474a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]   Unzipping tokenizers/punkt.zip.\n",
            "[nltk_data] Downloading package averaged_perceptron_tagger to\n",
            "[nltk_data]     /root/nltk_data...\n",
            "[nltk_data]   Unzipping taggers/averaged_perceptron_tagger.zip.\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "    <table border=\"1\">\n",
              "      <thead>\n",
              "        <tr>\n",
              "          <th>Serial No (of SHEROES)</th>\n",
              "          <th>hyperlink</th>\n",
              "          <th>Name</th>\n",
              "          <th>Count of Nouns</th>\n",
              "          <th>Count of Adjectives</th>\n",
              "        </tr>\n",
              "      </thead>\n",
              "      <tbody>\n",
              "        <tr>\n",
              "          <td>https://abcd2.projectabcd.com/display_the_dress.php?id=1</td>\n",
              "          <td>Namaste</td>\n",
              "          <td>Namasthe is a customary, non-contact form of Hindu greeting. Namaste is usually spoken with a slight bow and hands pressed together, palms touching and fingers pointing upwards. Namaste is used as a form of greeting, acknowledging, and welcoming a relative, guest, or stranger. In some contexts, it can be used to express gratitude for assistance offered or given and to thank people for their generosity. </td>\n",
              "          <td>18</td>\n",
              "          <td>5</td>\n",
              "        </tr>\n",
              "      </tbody>\n",
              "    </table>\n",
              "    "
            ]
          },
          "metadata": {}
        }
      ],
      "source": [
        "import nltk\n",
        "from IPython.display import display, HTML\n",
        "\n",
        "# Download NLTK resources\n",
        "nltk.download('punkt')\n",
        "nltk.download('averaged_perceptron_tagger')\n",
        "\n",
        "def count_nouns_and_adjectives(text):\n",
        "    tokens = nltk.word_tokenize(text)\n",
        "    tagged_tokens = nltk.pos_tag(tokens)\n",
        "\n",
        "    noun_count = 0\n",
        "    adjective_count = 0\n",
        "\n",
        "    for _, tag in tagged_tokens:\n",
        "        if tag.startswith('NN'):  # Nouns\n",
        "            noun_count += 1\n",
        "        elif tag.startswith('JJ'):  # Adjectives\n",
        "            adjective_count += 1\n",
        "\n",
        "    return noun_count, adjective_count\n",
        "\n",
        "def generate_html_table(description, did_you_know):\n",
        "    noun_count, adjective_count = count_nouns_and_adjectives(description)\n",
        "    html_table = f\"\"\"\n",
        "    <table border=\"1\">\n",
        "      <thead>\n",
        "        <tr>\n",
        "          <th>Serial No (of SHEROES)</th>\n",
        "          <th>hyperlink</th>\n",
        "          <th>Description</th>\n",
        "          <th>Count of Nouns</th>\n",
        "          <th>Count of Adjectives</th>\n",
        "        </tr>\n",
        "      </thead>\n",
        "      <tbody>\n",
        "        <tr>\n",
        "          <td>https://abcd2.projectabcd.com/display_the_dress.php?id=1</td>\n",
        "          <td>Namaste</td>\n",
        "          <td>{description}</td>\n",
        "          <td>{noun_count}</td>\n",
        "          <td>{adjective_count}</td>\n",
        "        </tr>\n",
        "      </tbody>\n",
        "    </table>\n",
        "    \"\"\"\n",
        "    return html_table\n",
        "\n",
        "# Input description and \"did_you_know\" text\n",
        "description = \"Namasthe is a customary, non-contact form of Hindu greeting. Namaste is usually spoken with a slight bow and hands pressed together, palms touching and fingers pointing upwards. Namaste is used as a form of greeting, acknowledging, and welcoming a relative, guest, or stranger. In some contexts, it can be used to express gratitude for assistance offered or given and to thank people for their generosity. \"\n",
        "did_you_know = \"The gesture of joining both hands has more than a symbolic meaning. It is said to provide a connection between the right and left hemispheres of the brain thus representing unification.\"\n",
        "\n",
        "# Generate HTML table\n",
        "html_table = generate_html_table(description, did_you_know)\n",
        "display(HTML(html_table))\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import nltk\n",
        "from IPython.display import display, HTML\n",
        "\n",
        "# Download NLTK resources\n",
        "nltk.download('punkt')\n",
        "nltk.download('averaged_perceptron_tagger')\n",
        "\n",
        "def count_nouns_and_adjectives(text):\n",
        "    tokens = nltk.word_tokenize(text)\n",
        "    tagged_tokens = nltk.pos_tag(tokens)\n",
        "\n",
        "    noun_count = 0\n",
        "    adjective_count = 0\n",
        "\n",
        "    for _, tag in tagged_tokens:\n",
        "        if tag.startswith('NN'):  # Nouns\n",
        "            noun_count += 1\n",
        "        elif tag.startswith('JJ'):  # Adjectives\n",
        "            adjective_count += 1\n",
        "\n",
        "    return noun_count, adjective_count\n",
        "\n",
        "def generate_html_table(description, did_you_know):\n",
        "    noun_count, adjective_count = count_nouns_and_adjectives(description)\n",
        "    html_table = f\"\"\"\n",
        "    <table border=\"1\">\n",
        "      <thead>\n",
        "        <tr>\n",
        "          <th>Serial No (of SHEROES)</th>\n",
        "          <th>ABCD ID</th>\n",
        "          <th>Name</th>\n",
        "          <th>Count of Nouns</th>\n",
        "          <th>Count of Adjectives</th>\n",
        "        </tr>\n",
        "      </thead>\n",
        "      <tbody>\n",
        "        <tr>\n",
        "          <td>1</td>\n",
        "          <td>Kurta Dupatta</td>\n",
        "          <td>{description}</td>\n",
        "          <td>{noun_count}</td>\n",
        "          <td>{adjective_count}</td>\n",
        "        </tr>\n",
        "      </tbody>\n",
        "    </table>\n",
        "    \"\"\"\n",
        "    return html_table\n",
        "\n",
        "# Input description and \"did_you_know\" text\n",
        "description = '''Kurta is a simple knee-length tunic dress that is worn across India. It can be paired with jeans, leggings, churidar, or salwar. Often this dress is worn with the dupatta (chunni), which is a shawl-like scarf that can be worn in several styles. The kurta dupatta combination comes in very simple styles and also with very intricate patterns.'''\n",
        "did_you_know = \"The kurta style became popular in India during the 1900s, but it is also worn in the U.S., U.K., Italy, France, and the Middle East.\"\n",
        "\n",
        "# Generate HTML table\n",
        "html_table = generate_html_table(description, did_you_know)\n",
        "display(HTML(html_table))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 227
        },
        "id": "S3RB6DBQbQBu",
        "outputId": "313535cd-ee97-4a3b-ad35-da5e2ba88ee6"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]   Package punkt is already up-to-date!\n",
            "[nltk_data] Downloading package averaged_perceptron_tagger to\n",
            "[nltk_data]     /root/nltk_data...\n",
            "[nltk_data]   Package averaged_perceptron_tagger is already up-to-\n",
            "[nltk_data]       date!\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "    <table border=\"1\">\n",
              "      <thead>\n",
              "        <tr>\n",
              "          <th>Serial No (of SHEROES)</th>\n",
              "          <th>ABCD ID</th>\n",
              "          <th>Name</th>\n",
              "          <th>Count of Nouns</th>\n",
              "          <th>Count of Adjectives</th>\n",
              "        </tr>\n",
              "      </thead>\n",
              "      <tbody>\n",
              "        <tr>\n",
              "          <td>1</td>\n",
              "          <td>Kurta Dupatta</td>\n",
              "          <td>Kurta is a simple knee-length tunic dress that is worn across India. It can be paired with jeans, leggings, churidar, or salwar. Often this dress is worn with the dupatta (chunni), which is a shawl-like scarf that can be worn in several styles. The kurta dupatta combination comes in very simple styles and also with very intricate patterns.</td>\n",
              "          <td>17</td>\n",
              "          <td>8</td>\n",
              "        </tr>\n",
              "      </tbody>\n",
              "    </table>\n",
              "    "
            ]
          },
          "metadata": {}
        }
      ]
    }
  ]
}