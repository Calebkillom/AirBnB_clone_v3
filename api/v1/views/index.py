#!/usr/bin/python3
""" index.py """
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """Return a JSON response with status: OK."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_object_counts_by_type():
    """Retrieve the number of each object by type."""

    """Create a dictionary to store object counts by type."""
    object_counts = {}

    """Define a mapping between class names and their attribute names."""
    class_to_attribute = {
        'Amenity': 'amenities',
        'City': 'cities',
        'Place': 'places',
        'Review': 'reviews',
        'State': 'states',
        'User': 'users'
    }

    """ Calculate the count of each object type and store it """
    for class_name, attribute_name in class_to_attribute.items():
        object_count = storage.count(class_name)
        object_counts[attribute_name] = object_count

    """ Return the count as a JSON response """
    return jsonify(object_counts)
