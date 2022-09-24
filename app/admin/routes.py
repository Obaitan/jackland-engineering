# from crypt import methods
from app.admin import bp
from flask import render_template, request, flash, redirect, url_for
from app.admin.forms import LoginForm, NewEquipmentForm, NewMaterialForm, NewProjectForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Project, Material, Equipment
from werkzeug.urls import url_parse


@bp.route('/', methods=['GET', 'POST'])
def login():
    title = 'Admin Login'
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password', category='danger')
            return redirect(url_for('admin.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('admin.dashboard')
        return redirect(next_page)
    return render_template('admin/login.html', title=title, form=form)


@bp.route('/dashboard')
@login_required
def dashboard():
    title = 'Admin Dashboard'
    project_no = len(Project.query.all())
    material_no = len(Material.query.all())
    equipment_no = len(Equipment.query.all())
    return render_template('admin/dashboard.html', title=title, project_no=project_no, material_no=material_no, equipment_no=equipment_no)


@bp.route('/projects')
@login_required
def projects():
    title = 'Admin Projects'
    projects = Project.query.all()
    return render_template('admin/projects.html', title=title, projects=projects)


@bp.route('projects/edit/<name>', methods=['GET', 'POST'])
@login_required
def edit_project(name):
    return render_template('admin/edit-project.html')


@bp.route('projects/delete/<name>', methods=['GET', 'POST'])
@login_required
def delet_project(name):
    pass


@bp.route('/project/new', methods=['GET', 'POST'])
@login_required
def new_project():
    title = 'Admin - New Project'
    form = NewProjectForm()
    return render_template('admin/new-project.html', title=title, form=form)


@bp.route('/materials')
@login_required
def materials():
    title = 'Admin Materials'
    materials = Material.query.all()
    return render_template('admin/materials.html', title=title, materials=materials)

@bp.route('materials/edit/<name>', methods=['GET', 'POST'])
@login_required
def edit_material(name):
    pass

@bp.route('materials/delete/<name>', methods=['GET', 'POST'])
@login_required
def delet_material(name):
    pass

@bp.route('/material/new', methods=['GET', 'POST'])
@login_required
def new_material():
    title = 'Admin - New Material'
    form = NewMaterialForm()
    return render_template('admin/new-material.html', title=title, form=form)


@bp.route('/equipment')
@login_required
def equipment():
    title = 'Admin Projects'
    equipment = Equipment.query.all()
    return render_template('admin/equipment.html', title=title, equipment=equipment)


@bp.route('equipment/edit/<name>', methods=['GET', 'POST'])
@login_required
def edit_equipment(name):
    pass

@bp.route('equipment/delete/<name>', methods=['GET', 'POST'])
@login_required
def delet_equipment(name):
    pass

@bp.route('/equipment/new', methods=['GET', 'POST'])
@login_required
def new_equipment():
    title = 'Admin - New Equipment'
    form = NewEquipmentForm()
    return render_template('admin/new-equipment.html', title=title, form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))