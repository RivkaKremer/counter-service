#aws eks update-kubeconfig --name=rivka-kremer-cluster
#<pesonal_git_token>
flux bootstrap github \
  --components-extra=image-reflector-controller,image-automation-controller \
  --owner=RivkaKremer \
  --repository=counter-service \
  --branch=check-point-task \
  --path=./k8s-app-components \
  --token-auth \
  --personal