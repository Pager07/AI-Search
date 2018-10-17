import os
from tflearn.data_utils import image_preloader
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np







train_frac = 0.7
vlad_frac = 0.1
testing_frac = 0.2

#data-dimensions
img_size_flat = 784
#gray_scale = 1 channels
num_channels = 1
#image_shape gotten grom x_trai[0].shape
img_size = 28
img_shape = (28,28)
num_classes = 2
#loadig data 
main_trainfile  = "/Users/sandeep/Downloads/all/train"
train_textfile = "/Users/sandeep/Downloads/all/training_data.txt"
test_textfile = "/Users/sandeep/Downloads/all/testing_data.txt"
vald_textfile = "/Users/sandeep/Downloads/all/validation_data.txt"

#loading images names in a list
image_name_list= os.listdir(main_trainfile)

#split the images into TRAIN =  TRAIN, VAliDATION , TEST
#image_preloader() function helps us to load image at fly
#requires a text file with path "imagefloder+fileName+(space)class"

#hence prep a textfile "imagefloder+fileName+(space)class"

total_num_images = len(image_name_list)

######writing train textfile 
train_textfile_pointer = open(train_textfile ,'w')
train_images_list = image_name_list[0: int(train_frac*total_num_images)]
for image_name in train_images_list:
    if image_name[0:3] == "cat":
        string = main_trainfile+ "/" + image_name + " 0\n"
        train_textfile_pointer.write(string)
    elif image_name[0:3] == "dog":
        string = main_trainfile+ "/" + image_name + " 1\n"
        train_textfile_pointer.write(string)

train_textfile_pointer.close()

####writing ttesting textfile
f = open(test_textfile ,'w')
testing_images_list = image_name_list[int(train_frac*total_num_images): int((train_frac + testing_frac)*total_num_images)]
for image_name in testing_images_list:
    if image_name[0:3] == "cat":
        string = main_trainfile+ "/" + image_name + " 0\n"
        f.write(string)
    elif image_name[0:3] == "dog":
        string= main_trainfile+ "/" + image_name + " 1\n"
        f.write(string)

f.close()


####writing validation textfile
f = open(vald_textfile ,'w')
vald_images_list = image_name_list[int((train_frac + testing_frac)*total_num_images) : total_num_images]
for image_name in vald_images_list:
    if image_name[0:3] == "cat":
        string = main_trainfile+ "/" + image_name + " 0\n"
        
        f.write(string)
    elif image_name[0:3] == "dog":
        string_list= main_trainfile+ "/" + image_name + " 1\n"
        string = "".join(str(x) for x in string_list)
        f.write(string)

f.close()

#########'
##Now use image_preloader to import images
#image_preloader returns 2 array X,Y ; x is images array and y the labels array
#using this; get X_train ,X_test and X_vald array of images and their corresponding lables
x_train , y_train = image_preloader(train_textfile,
                                    image_shape = (28,28),
                                    mode = 'file',
                                    categorical_labels = True , 
                                    normalize = True,
                                    grayscale = True 
                                    )

x_test, y_test = image_preloader(test_textfile,
                                    image_shape = (28,28),
                                    mode = 'file',
                                    categorical_labels = True , 
                                    normalize = True,
                                    grayscale = True 
                                    )



x_vald, y_vald = image_preloader(vald_textfile,
                                    image_shape = (28,28),
                                    mode = 'file',
                                    categorical_labels = True , 
                                    normalize = True,
                                    grayscale = True 
                                    )

print("Dataset loaded Successfully!")
print("Number of images total {}".format(total_num_images))
print("Number of training images: {}".format(len(x_train)))
print("Number of testing images: {}".format(len(x_test)))
print("Number of validationg images: {}".format(len(x_vald)))

#def image_array_flatten(image_list):
#    flatten_image_list = [image.flatten() for image in image_list]
#    return flatten_image_list
#    
#
#def new_weight(shape):
#    weigth = tf.truncated_normal(shape , stddev = 0.05)
#    weigth_matrix = tf.Variable(weigth)
#    return(weigth_matrix)
#
#def new_bias(length):
#    bias = tf.constant(0.05 , shape =[length])
#    bias_vector = tf.Variable(bias)
#    return bias_vector
#
##pass in info required to make filter:(input , output) or filter=(num_input_channels , filter_size)*num_of_filters
#    #info required: (num_input_channels , filter_size)*num_of_filters
#    #its all most like filter =(input,output) 
#    #input = images =num_of_input_channels , filter_size)
#    #output = num_filters
##pass in input ofcourse
#
##doing pooling or not (ask last conv or not using bool)
#def new_conv_layer(input , num_input_channels , filter_size , num_filters , use_pooling):
#    weigth = new_weight([filter_size , filter_size , num_input_channels , num_filters])
#    bias = new_bias(num_filters)
#    
#    #to do conv we need:(input->padding) , (filter->stride) 
#    layer = tf.nn.conv2d(input = input ,
#                         filter = weigth,
#                         padding = "SAME",
#                         strides = [1,1,1,1])
#    
#    layer = layer + bias 
#    
#    if use_pooling:
#        #to do pool we need: (input->padding) , (window - > stride and size)
#        layer = tf.nn.max_pool(value = layer , 
#                               padding ="SAME",
#                               ksize = [1,2,2,1] , 
#                               strides = [1,2,2,1])
#        
#    layer = tf.nn.relu(layer)
#    
#    return layer ,weigth
#
#
#def flatten_layer(layer):
#    #conv laye and poool will give [num_of_images , filter_size , filter_size , num_inputchannnle]
#    # after covn and pool: image = filter_size , num_inputchannnle
#    #do conversion: iamge = featuers 
#    #features = filter_size* num_input_channels 
#    
#    layer_shape = layer.get_shape()
#    
#    num_features = layer_shape[1:4].num_elements()
#    
#    layer_flat = tf.reshape(layer , [-1 , num_features])
#    
#    return layer_flat ,num_features
#
##pass in info required to make filter: (input , output)
#    #infoo reuqired: filter = (num_of_featuers , num_classes)
##pass in input ofcurse
##do relu or not? (asking if its last fc layer)
#    
#    
#def new_fc_layer(input , num_inputs , num_outputs , use_relu = True):
#    
#    weigth = new_weight([num_inputs , num_outputs])
#    bias = new_bias(length = num_outputs)
#    
#    layer = tf.matmul(input , weigth) + bias
#    
#    if use_relu:
#        layer = tf.nn.relu(layer)
#        
#    return layer
#
#def plot_image(image):
#    plt.imshow(image.reshape(img_shape),
#               interpolation='nearest',
#               cmap='binary')
#
#    plt.show()
#
#
#
#
#x = tf.placeholder(tf.float32 , shape=[None , img_size_flat] , name ='x')
##convert placeholder to 4D
#x_image = tf.reshape(x , [-1 ,img_size , img_size , num_channels])
#
##make a class placeholder 
##we need class *how many
#y_true = tf.placeholder(tf.float32, shape=[None , num_classes] , name = 'y_true')
#
#y_true_cls = tf.argmax(y_true , axis=1)
#
#
##create 1st conv1 layer
##pass in (input, requiredfilterinfo , askforpooling)
#filter_size1 = 5 
#num_filter1 = 16 
#layer_conv1 , weights_conv1 = new_conv_layer(input = x_image ,
#                                             num_input_channels = num_channels,
#                                             filter_size  =filter_size1,
#                                             num_filters = num_filter1,
#                                             use_pooling = True)
#
#
#
#filter_size2 = 5
#num_filters2 = 36
##expect laayer_conv2 shape = (?, 7, 7, 36)
##image= (7,7) width and heigth
##36= num of channels (one for each filter) or basically how many image clones
##? = number of different images
#layer_conv2 , weights_conv2 = new_conv_layer(input = layer_conv1 , 
#               num_input_channels = num_filter1,
#               filter_size = filter_size2,
#               num_filters = num_filters2,
#               use_pooling = True)
#
#
##Each image will give featuers 
##expect (7*7) featuers for each image * 36 for all the clones 
##hence featuers = (7*7)*36
#layer_flat , num_features = flatten_layer(layer_conv2)
#
#fc_size = 128
###num_input = num of featuresa ofcourse
##num_output = 128 (dont know how) but it will sever as num_inputes in next layer
#layer_fc1 = new_fc_layer(input = layer_flat,
#             num_inputs = num_features,
#             num_outputs = fc_size,
#             use_relu =True)
#
##num_input == num_output in last layer
##num_output == num_classes (because it is last fc layer)
##the last fc layer result is also called logits
#layer_fc2 = new_fc_layer(input = layer_fc1, 
#                         num_inputs = fc_size,
#                         num_outputs = num_classes,
#                         use_relu = False
#                         )
##y_pred/matrix form of proobablities  
#y_pred = tf.nn.softmax(layer_fc2)
#
#y_pred_cls = tf.argmax(y_pred , axis = 1)
#
######NOW COST FUNCTION
#
#cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits = layer_fc2,
#                                        labels= y_true)
#
#cost = tf.reduce_mean(cross_entropy)
#
#optimizer = tf.train.AdamOptimizer(learning_rate = 1e-4).minimize(cost)
#
#
##this will retuern a boolean value
##ex[false, true,falase.....] seeing if the actucal class matches the real class
#correctly_predicted = tf.equal(y_pred_cls,y_true_cls)
#
#correctly_predicted_to_binary= tf.cast(correctly_predicted , tf.float32)
#accuracy= tf.reduce_mean(correctly_predicted_to_binary)
#
#
##Creating a pointer  in our graph graph
#session = tf.Session()
#
##creating a node which will initalise all variables
#
#var_initializer = tf.global_variables_initializer()
#
##point the pointer to the variable initializer node
#session.run(var_initializer)
#
#
#
##running interation
#batch_size = 20
#num_iteration = len(x_train)/batch_size
#epoch = 1
#
#num_test_samples = len(x_test)
#num_vald_samples = len(x_vald)
#
#for epoch_iteration in range(epoch):
#    print("Epoch Iteration number:{}".format(epoch_iteration))
#    
#    previous_batch = 0
#    
#    for iteration in range(num_iteration):
#        
#        current_batch = previous_batch + batch_size
#        
#        input_images = x_train[previous_batch : current_batch]
#        input_images_reshaped = np.reshape(input_images , [batch_size,784])
#        
#        input_labels = y_train[previous_batch : current_batch]
#        input_labels_reshaped = np.reshape(input_labels , [batch_size,2])
#        
#        previous_batch = previous_batch + batch_size
#        
#        feed_dict_train = {x: input_images_reshaped,
#                           y_true : input_labels_reshaped}
#        
#        session.run(optimizer , feed_dict = feed_dict_train)
#        
#        
#        if iteration % 100 == 0:
#            acc = session.run(accuracy , feed_dict = feed_dict_train)
#            message = "Epoch :{} , Iteration:{} ,Accuracy:{} ".format(epoch_iteration , iteration , acc)
#            print(message)
#                       
#         
#
#
########test
#    input_images_test = x_test[0:num_test_samples]
#    input_images_test_reshaped = np.reshape(input_images_test ,[num_test_samples,784])
#    input_labels_test = y_test[0:num_test_samples]
#    input_labels_test_reshaped =np.reshape(input_labels_test , [num_test_samples,2])
#    
#    feed_dict_test = {x: input_images_test_reshaped,
#                      y_true : input_labels_test_reshaped}
#    acc_test = session.run(accuracy , feed_dict = feed_dict_test)
#    
########valditaion
#    input_images_vald = x_vald[0:num_vald_samples]
#    input_images_vald_reshaped = np.reshape(input_images_vald ,[num_vald_samples,784])
#    input_labels_vald = y_vald[0:num_vald_samples]
#    input_labels_vald_reshaped =np.reshape(input_labels_vald , [num_vald_samples,2])
#     
#    feed_dict_vald = {x: input_images_vald_reshaped,
#                         y_true : input_labels_vald_reshaped}
#       
#    acc_vald = session.run(accuracy , feed_dict = feed_dict_vald)
#    
#    print("Accuracy :: Test-Set {} , Validation-Set {} ".format(acc_test , acc_vald))
#   
#      
#       
#            
##def process_img(img):
##        img=img.resize((28, 28), Image.ANTIALIAS) #resize the image
##        img = img.convert(mode = 'L')
##        img = np.array(img)
##        img=img/np.max(img).astype(float) 
##        img=np.reshape(img, [1,784])
##        return img   
#myimages_textfile = '/Users/sandeep/Downloads/all/myimages .txt'
#num_myimages = 2
#myimages_x , myimages_y = image_preloader(myimages_textfile,
#                                    image_shape = (28,28),
#                                    mode = 'file',
#                                    categorical_labels = True , 
#                                    normalize = True,
#                                    grayscale = True 
#                                    )
#
#myimages_x_reshaped = np.reshape(myimages_x , [num_myimages , 784])
#feed_dict_myimage = {x:myimages_x_reshaped}
#
#predicted_class= session.run(y_pred_cls, feed_dict=feed_dict_myimage)
#
#for i in predicted_class:
#    plot_image(myimages_x[i])
#    if predicted_class[i] == 0:
#        print("It is a Cat!")
#    else: 
#        print("It is a Dog!")
#
#
#
#
#
#
#
#
#
#
#
#
#    
#    
#    
#    
#
#
#    
#    
#    
#    
#    
#
#


