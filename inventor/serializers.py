from rest_framework import serializers
from .models import User,inventions,investment



class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = ['username','first_name', 'last_name', 'email_address', 'phone','country', 'is_inventor']


class InvestorCustomRegistrationSerializer(serializers.ModelSerializer):

        password2 = serializers.CharField(style ={"input_type":"password"}, write_only=True)
        #password = serializers.CharField(style ={"input_type":"password"}, write_only=True)
        class Meta:
                model = User
                fields = ['username','first_name', 'last_name', 'email_address','password', 'password2', 'phone', 'country']
                extra_kwargs = {'password': {'write_only': True}}
                

        def save(self, **kwargs):
            user = User(
                username =self.validated_data['username'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                email_address=self.validated_data['email_address'],
                phone=self.validated_data['phone'],
                country=self.validated_data['country'],
            )

            password=self.validated_data['password'],
            password2=self.validated_data['password2'],
            if password!=password2:
                raise serializers.ValidationError({"error":"password does not match"})


            user.set_password(self.validated_data['password'],)
            user.is_investor=True
            user.save()
            #investor.objects.create(user=user)
            return user



class InventorCustomRegistrationSerializer(serializers.ModelSerializer):
    
        password2 = serializers.CharField(style ={"input_type":"password"}, write_only=True)
        #password = serializers.CharField(style ={"input_type":"password"}, write_only=True)
        class Meta:
                model = User
                fields = ['username','first_name', 'last_name', 'email_address','password', 'password2', 'phone', 'country']
                extra_kwargs = {'password': {'write_only': True}}
                

        def save(self, **kwargs):
            user = User(
                username =self.validated_data['username'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                email_address=self.validated_data['email_address'],
                phone=self.validated_data['phone'],
                country=self.validated_data['country'],
            )

            password=self.validated_data['password'],
            password2=self.validated_data['password2'],
            if password!=password2:
                raise serializers.ValidationError({"error":"password does not match"})


            user.set_password(self.validated_data['password'],)
            user.is_inventor=True
            user.save()
            #inventor.objects.create(user=user)
            return user


class InvestorUpdateSerializer(serializers.ModelSerializer):

        #password2 = serializers.CharField(style ={"input_type":"password"}, write_only=True)
        #password = serializers.CharField(style ={"input_type":"password"}, write_only=True)
        class Meta:
                model = User
                fields = ['id','image','first_name', 'last_name','phone', 'country', 'state','company_name','company_email', 'company_address', 'head_office','hobbies', 'url','facebook_url', 'linkedin_url']

        def create(self, validated_data):
            return User.objects.create(**validated_data)
                

        def update(self, instance, validated_data):
            instance.image = validated_data.get('image', instance.image)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.country = validated_data.get('country', instance.country)
            instance.state = validated_data.get('state', instance.state)
            instance.company_name = validated_data.get('company_name', instance.company_name)
            instance.company_email = validated_data.get('company_email', instance.company_email)
            instance.company_address = validated_data.get('company_address', instance.company_address)
            instance.head_office = validated_data.get('head_office', instance.head_office)
            instance.hobbies = validated_data.get('hobbies', instance.hobbies)
            instance.url= validated_data.get('url', instance.url)
            instance.facebook_url = validated_data.get('facebook_url', instance.facebook_url)
            instance.linkedin_url = validated_data.get('linkedin_url', instance.linkedin_url)

            instance.save()

            return instance



class InventorUpdateSerializer(serializers.ModelSerializer):

        #password2 = serializers.CharField(style ={"input_type":"password"}, write_only=True)
        #password = serializers.CharField(style ={"input_type":"password"}, write_only=True)
        class Meta:
                model = User
                fields = ['id','image','first_name', 'last_name','phone', 'country', 'state','company_name','company_email', 'company_address', 'head_office','hobbies', 'url','facebook_url', 'linkedin_url']
        

        """def create(self, validated_data):
            return User.objects.create(**validated_data)
        """
        def validate_username(self, value):
            user = self.context['request'].user
            if User.objects.exclude(pk=user.pk).filter(username=value).exists():
                raise serializers.ValidationError({"username": "This username is already in use"})
            return value
                

        def update(self, instance, validated_data):

            instance.image = validated_data.get('image', instance.image)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.country = validated_data.get('country', instance.country)
            instance.state = validated_data.get('state', instance.state)
            instance.company_name = validated_data.get('company_name', instance.company_name)
            instance.company_email = validated_data.get('company_email', instance.company_email)
            instance.company_address = validated_data.get('company_address', instance.company_address)
            instance.head_office = validated_data.get('head_office', instance.head_office)
            instance.hobbies = validated_data.get('hobbies', instance.hobbies)
            instance.url = validated_data.get('url', instance.url)
            instance.facebook_url = validated_data.get('facebook_url', instance.facebook_url)
            instance.linkedin_url = validated_data.get('linkedin_url', instance.linkedin_url)

            instance.save()

            return instance




class InventionSerializer(serializers.ModelSerializer):

        
        class Meta:
                model = inventions
                fields = ['id', 'inventor', 'inventor_name', 'published_date', 'description', 'invention_name', 'invention_caption','industry', 'related_industry', 'sum_required_to_complete', 'tag', 'additional_details', 'equity_per_invest', 'invention_url', 'invention_timeline', 'current_budget', 'target_audience', 'business_model', 'inventor_image', 'invention_image', 'revenue_generating_stractegy', 'expansion_plans', 'required_amount', 'amount_needed_to_start', 'equity_per_invest', 'currency']
        

    #Fill in all required serializer values
        def create(self, validated_data):
            return inventions.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.inventor_name = validated_data.get('inventor_name', instance.inventor_name)
            instance.inventor = validated_data.get('inventor', instance.inventor)
            instance.published_date = validated_data.get('published_date', instance.published_date)
            instance.description = validated_data.get('description', instance.description)
            instance.invention_name = validated_data.get('invention_name', instance.invention_name)
            instance.invention_caption = validated_data.get('invention_caption', instance.invention_caption)
            #instance.banner = validated_data.get('banner', instance.banner)
            instance.industry = validated_data.get('industry', instance.industry)
            instance.related_industry = validated_data.get('related_industry', instance.related_industry)
            instance.sum_required_to_complete = validated_data.get('sum_required_to_complete', instance.sum_required_to_complete)
            instance.tag = validated_data.get('tag', instance.tag)
            #instance.gallery = validated_data.get('gallery', instance.gallery)
            instance.additional_details = validated_data.get('additional_details', instance.additional_details)
            instance.equity_per_invest = validated_data.get('equity_per_invest', instance.equity_per_invest)
            instance.invention_url = validated_data.get('invention_url', instance.invention_url)
            instance.invention_timeline = validated_data.get('invention_timeline', instance.invention_timeline)
            instance.target_audience = validated_data.get('target_audience', instance.target_audience)
            instance.business_model = validated_data.get('business_model', instance.business_model)
            instance.revenue_generating_stractegy = validated_data.get('revenue_generating_stractegy', instance.revenue_generating_stractegy)
            instance.expansion_plans = validated_data.get('expansion_plans', instance.expansion_plans)
            instance.required_amount = validated_data.get('required_amount', instance.required_amount)
            instance.amount_needed_to_start = validated_data.get('amount_needed_to_start', instance.amount_needed_to_start)
            instance.currency = validated_data.get('currency', instance.currency)
            instance.invention_image = validated_data.get('invention_image', instance.invention_image)
            instance.inventor_image = validated_data.get('inventor_image', instance.inventor_image)
            
            

            
            
            

            instance.save()

            return instance


class Trimmedinventions(serializers.ModelSerializer):
    class Meta:
        model = inventions
        fields = ['id', 'inventor_name', 'inventor_image', 'invention_name', 'invention_image', 'description', 'published_date', 'required_amount' ]



class InvestmentSerializer(serializers.ModelSerializer):

        
        class Meta:
                model = investment
                fields = ['id','Invents','amount',]

        




