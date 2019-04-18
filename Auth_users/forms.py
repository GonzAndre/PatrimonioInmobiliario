class LeadershipForm(ModelForm):
    class Meta:
        model = Leadership
        fields = ['username', 'first_name', 'last_name', 'password', 'work_position', 'mail']