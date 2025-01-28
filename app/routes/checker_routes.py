from flask import Blueprint, request, abort

from app.services.calculations import calculate_cross_sums

bp = Blueprint('checker_routes', __name__)

@bp.route('/check', methods=['POST'])
def check_answer():
    data = request.json
    if "row_targets" not in data or "col_targets" not in data or "row_weights" not in data or "col_weights" not in data:
        abort(400)
        
    return calculate_cross_sums(data["row_targets"], data["col_targets"], data["row_weights"], data["col_weights"])
    
    

