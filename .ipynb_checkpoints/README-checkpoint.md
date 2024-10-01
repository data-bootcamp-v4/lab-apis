![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# LAB | APIs
<details>
  <summary>
   <h2>Learning Goals</h2>
  </summary>

  This lab allows you to practice and apply the concepts and techniques taught in class. 

  Upon completion of this lab, you will be able to:
  
- Use Python libraries such as requests to extract data from APIs, and convert extracted data into a suitable data structure.

  <br>
  <hr> 

</details>

<details>

</details>


## Introduction

Welcome to the world of music data exploration! In this lab, you will venture into the realm of the Spotify API using SpotiPy, a Python library that allows you to interact with Spotify's vast music catalog and playlist data.

### **Objective**

The objective of this lab is to acquaint you with the fundamental operations of the Spotify API using SpotiPy. You will learn how to authenticate with the API, perform searches for tracks and artists, and retrieve information about playlists, among other things.

### **Lab Sections**

This lab comprises two main sections:

#### **Section 1: Discovering New Music through Your Favorite Artists**

In this section, you will use the Spotify API to explore the top tracks of your favorite artists and discover related artists. By the end, you'll have the opportunity to create a playlist featuring your favorite tracks and those of related artists.

#### **Section 2: Unraveling the World of Playlists**

In the second section, you will delve into Spotify's featured playlists. You'll learn how to fetch information about these playlists, explore their details, and extract track and artist data from them.

<br>

Let's embark on this musical journey into the world of Spotify API exploration!

<br>

**Happy coding!** :heart:


## Requirements

- Fork this repo
- Clone it to your machine

## Getting Started

Complete the challenges in the `Jupyter Notebook` file. Follow the instructions and add your code and explanations as necessary.

## Submission

- Upon completion, run the following commands:

```bash
git add .
git commit -m "Solved lab"
git push origin master
```

- Paste the link of your lab in Student Portal.


## FAQs
<details>
  <summary>I am stuck in the exercise and don't know how to solve the problem or where to start.</summary>
  <br>

  If you are stuck in your code and don't know how to solve the problem or where to start, you should take a step back and try to form a clear question about the specific issue you are facing. This will help you narrow down the problem and come up with potential solutions.


  For example, is it a concept that you don't understand, or are you receiving an error message that you don't know how to fix? It is usually helpful to try to state the problem as clearly as possible, including any error messages you are receiving. This can help you communicate the issue to others and potentially get help from classmates or online resources. 


  Once you have a clear understanding of the problem, you will be able to start working toward the solution.

  [Back to top](#faqs)

</details>


<details>
  <summary>I am unable to push changes to the repository. What should I do?</summary>
  <br>

There are a couple of possible reasons why you may be unable to *push* changes to a Git repository:

1. **You have not committed your changes:** Before you can push your changes to the repository, you need to commit them using the `git commit` command. Make sure you have committed your changes and try pushing again. To do this, run the following terminal commands from the project folder:
  ```bash
  git add .
  git commit -m "Your commit message"
  git push
  ```
2. **You do not have permission to push to the repository:** If you have cloned the repository directly from the main Ironhack repository without making a *Fork* first, you do not have write access to the repository.
To check which remote repository you have cloned, run the following terminal command from the project folder:
  ```bash
  git remote -v
  ```
If the link shown is the same as the main Ironhack repository, you will need to fork the repository to your GitHub account first and then clone your fork to your local machine to be able to push the changes.

**Note**: You should make a copy of your local code to avoid losing it in the process.

  [Back to top](#faqs)

</details>

