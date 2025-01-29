from flask import Blueprint, request, abort

from app.services.calculations import calculate_cross_sums

bp = Blueprint('checker_routes', __name__)

@bp.route('/check', methods=['POST'])
def check_answer():
    data = request.json
    if "row_targets" not in data or "col_targets" not in data or "row_weights" not in data or "col_weights" not in data:
        return "Some attributes missing", 400

    
    if len(data["row_targets"]) != len(data["col_targets"]):
         return "Targets not same length", 400
    
    grid_size = len(data["col_targets"])

    if not correct_grid_size(grid_size, data["row_weights"], data["col_weights"]):
        return "Grid size error", 400

        
    return calculate_cross_sums(data["row_targets"], data["col_targets"], data["row_weights"], data["col_weights"])

def correct_grid_size(grid_size, row_weights, col_weights):
    if len(row_weights) != grid_size or len(col_weights) != grid_size:
        return False
    
    for i in range(grid_size):
        if len(row_weights[i]) != grid_size or len(col_weights[i]) != grid_size:
            return False
    return True
    
    

