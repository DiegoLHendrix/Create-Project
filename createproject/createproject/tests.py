from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        """Check if the home page responds with a 200 OK status."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        """Check if the home page uses home.html and extends base.html."""
        response = self.client.get(reverse("home"))
        # Update this line to include the folder prefix:
        self.assertTemplateUsed(response, "createproject/home.html")
        self.assertContains(response, "Welcome to my Website!")

    def test_homepage_context_data(self):
        """Ensure the view passes the features and projects lists to the template."""
        response = self.client.get("/")
        self.assertTrue("features" in response.context)
        self.assertTrue("projects" in response.context)
        
        # You can even check if the data has specific items
        features = response.context["features"]
        self.assertGreater(len(features), 0)
        
    def test_homepage_elements(self):
        response = self.client.get("/")
        # Test the browser tab title
        self.assertContains(response, "<title>Home Page</title>")
        # Test that the carousel is present by its ID
        self.assertContains(response, 'id="featureCarousel"')
        # Test that your projects are rendering
        self.assertContains(response, "Latest Projects")