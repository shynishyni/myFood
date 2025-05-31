# myFood

# **🍽️ Recipe API**

This API allows users to:

* **Add new recipes** with images, ingredients, steps, and details.
* **Fetch all recipes**.
* **Get a specific recipe** by ID.
* **Search recipes** by area.

## 🌐 Base URL

```
http://<your-domain>/
```

Example (local):

```
http://127.0.0.1:8000/
```

---

## 📦 Endpoints

### 1️⃣ Add a Recipe

* **URL:** `/addrecipe`
* **Method:** `POST`
* **Content-Type:** `multipart/form-data`
* **Body Parameters (Form Data):**

  | Field    | Type         | Required | Description                      |
  | -------- | ------------ | -------- | -------------------------------- |
  | name     | String       | ✅        | Name of the recipe               |
  | area     | String       | ✅        | Recipe origin area               |
  | writer   | String       | ✅        | Name of the recipe author        |
  | category | String       | ✅        | Recipe category (e.g., Dessert)  |
  | quotes   | JSON string  | ✅        | A JSON string with recipe quotes |
  | step1-10 | String       | Optional | Step-by-step instructions        |
  | ing1-15  | String       | Optional | Ingredients                      |
  | pic1     | File (Image) | ✅        | Recipe image 1                   |
  | pic2     | File (Image) | ✅        | Recipe image 2                   |

✅ = Required

* **Example Request (Postman form-data):**

  ```
  name: "Mango Cake"
  area: "India"
  writer: "John Doe"
  category: "Dessert"
  quotes: {"inspiration": "A delicious mango cake for summer!"}
  step1: "Preheat oven to 350°F."
  ing1: "2 cups flour"
  pic1: (attach image)
  pic2: (attach image)
  ```

* **Response:**

  ```json
  {
    "recipy": "Recipe added successfully"
  }
  ```

---

### 2️⃣ Get All Recipes

* **URL:** `/getallrecipes`

* **Method:** `GET`

* **Response Example:**

  ```json
  [
    {
      "id": 1,
      "name": "Mango Cake",
      "area": "India",
      "writer": "John Doe",
      "category": "Dessert",
      "quotes": {"inspiration": "A delicious mango cake for summer!"},
      "step1": "Preheat oven to 350°F.",
      "ing1": "2 cups flour",
      ...
      "pic1": "/media/food_images/mango1.jpg",
      "pic2": "/media/food_images/mango2.jpg"
    },
    ...
  ]
  ```

---

### 3️⃣ Get Recipe by ID

* **URL:** `/getrecipe/<id>`

* **Method:** `GET`

* **Path Parameter:**

  * `id` (int) - Recipe ID.

* **Response Example (Success):**

  ```json
  {
    "id": 1,
    "name": "Mango Cake",
    ...
  }
  ```

* **Response Example (Not Found):**

  ```json
  {
    "message": "Item not found :("
  }
  ```

---

### 4️⃣ Get Recipes by Area

* **URL:** `/getsomerecipe/<area>`

* **Method:** `GET`

* **Path Parameter:**

  * `area` (string) - Recipe area (e.g., "India", "Italy", or use `All` to fetch all recipes).

* **Response Example:**

  ```json
  [
    {
      "id": 2,
      "name": "Pasta Carbonara",
      "area": "Italy",
      ...
    }
  ]
  ```

* **Response Example (Not Found):**

  ```json
  {
    "message": "Item not found"
  }
  ```

---

## 🛠️ Setup Instructions

1. **Install requirements:**

   ```
   pip install django djangorestframework pillow
   ```

2. **Add media settings to `settings.py`:**

   ```python
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```

3. **Configure URLs (`urls.py`):**

   ```python
   from django.conf import settings
   from django.conf.urls.static import static

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('addrecipe', views.recipes, name='addrecipe'),
       path('getallrecipes', views.recipes, name='getallrecipes'),
       path('getrecipe/<int:id>', views.getrecipe, name='getrecipe'),
       path('getsomerecipe/<str:area>', views.getbyarea, name='getsomerecipe'),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

4. **Migrate database:**

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run server:**

   ```
   python manage.py runserver
   ```

---

## 📌 Notes

* **Image Uploads:** Uploaded images are stored in the `media/food_images/` directory.
* **Media URL Handling:** Ensure media files are served correctly in development using `MEDIA_URL` and `MEDIA_ROOT`.
* **Error Handling:** API returns `404` for not found cases and `500` for server errors.

