# ProductMgmtSystem
This is the Demo Project for learning Django's Rest-Framework and Rest-Api. Here, I have used ViewSet class of rest_framework.

## ViewSets

- Viewset allows you to combine the logic for a set of related views in a single class, through ViewSet. 
- A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), but provides actions such as .list() and .create().
- ViewSets can speed-up the development and better maintainability. 

1.  ViewSet
2.  GenericViewSet
3.  ModelViewSet

#### 1. ViewSet

- The ViewSet class inherits from APIView.
- We can use the standard attributes such as permission_classes, authentication_classes in order to control the API policy on the viewset.

#### 2. GenericViewSet

- The GenericViewSet class inherits from GenericAPIView.
- It provides the default set of get_object, get_queryset methods and other generic view base behavior, but does not include any actions by default.
- The difference between ViewSet and GenericViewSet is that it provides generic methods like get_object and get_queryset.

#### 3. ModelViewSet

- The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, by mixing in the behavior of the various mixin classes. 

- The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy().

- Most of the times we use this because it provides the generic functionality so, we simply need to override the attributes like queryset , serializer_class , permission_classesand authentication_classes.

- If we any conditional logic then we can override methods like get_object, get_queryset, get_permission_classes, etc.

## Advantages of ViewSet over View Class

- Repeated logic can be combined into a single class. 
- By using routers, we no longer need to deal with wiring up the URL conf ourselves.
